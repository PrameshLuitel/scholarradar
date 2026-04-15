"""
Groq LLM Cascade — Tries multiple Groq-hosted models in sequence to
guarantee a response even when individual models are rate-limited.

Cascade order (best quality → unlimited fallback):
  1. openai/gpt-oss-120b      — best reasoning
  2. openai/gpt-oss-20b       — lighter, same family
  3. qwen/qwen3-32b           — strong alternative
  4. llama-3.3-70b-versatile   — proven reliable  
  5. groq/compound             — unlimited, never fails

Each model is tried in order. On 429 / 503 / model error, we immediately
fall through to the next one.  `compound` is the safety net — it is
unlimited and uses Groq's agentic routing.
"""

from __future__ import annotations

import os
import json
import time
from typing import AsyncGenerator, Optional

import httpx
import structlog

log = structlog.get_logger("utils.groq_cascade")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Cascade order — first model that succeeds wins
# We prioritize TPM (Tokens Per Minute) room so large CVs don't crash
MODELS = [
    "groq/compound",                           # 70K TPM — best for deep context
    "meta-llama/llama-4-scout-17b-16e-instruct", # 30K TPM — extremely fast/roomy
    "llama-3.3-70b-versatile",                 # 12K TPM — balanced fallback
    "openai/gpt-oss-120b",                     # 8K TPM  — reasoning fallback
    "openai/gpt-oss-20b",                      # 8K TPM  — secondary reasoning
    "qwen/qwen3-32b",                          # 6K TPM  — alternative fallback
]

# Token pricing per 1M tokens (for cost tracking)
MODEL_PRICING = {
    "openai/gpt-oss-120b":    {"input": 0.15, "output": 0.60},
    "openai/gpt-oss-20b":     {"input": 0.15, "output": 0.60},  # ~same family
    "qwen/qwen3-32b":         {"input": 0.29, "output": 0.59},
    "llama-3.3-70b-versatile": {"input": 0.59, "output": 0.79},
    "groq/compound":          {"input": 0.15, "output": 0.60},  # varies
}

# Errors that indicate rate limiting / temporary unavailability
RETRY_STATUS_CODES = {429, 503, 502, 500}


def _get_api_key() -> str:
    key = os.getenv("GROQ_API_KEY", "")
    if not key:
        raise ValueError("GROQ_API_KEY not set in environment variables")
    return key


async def stream_groq_response(
    system_prompt: str,
    user_prompt: str,
    max_tokens: int = 4096,
    temperature: float = 0.7,
) -> AsyncGenerator[dict, None]:
    """
    Stream a response from Groq, cascading through models on failure.

    Yields dicts with keys:
      - {"type": "model", "model": "..."} — which model is being used
      - {"type": "chunk", "content": "..."} — a text chunk
      - {"type": "done", "model": "...", "usage": {...}, "cost_usd": ...}
      - {"type": "error", "message": "..."} — if all models failed
    """
    api_key = _get_api_key()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    last_error = None

    for model in MODELS:
        log.info("groq_cascade_trying", model=model)

        try:
            async with httpx.AsyncClient(timeout=180.0) as client:
                response = await client.post(
                    GROQ_API_URL,
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": model,
                        "messages": messages,
                        "max_tokens": max_tokens,
                        "temperature": temperature,
                        "stream": True,
                    },
                )

                if response.status_code in RETRY_STATUS_CODES:
                    error_text = response.text[:200]
                    log.warning(
                        "groq_cascade_rate_limited",
                        model=model,
                        status=response.status_code,
                        error=error_text,
                    )
                    last_error = f"{model}: HTTP {response.status_code}"
                    continue

                if response.status_code != 200:
                    error_text = response.text[:200]
                    log.warning(
                        "groq_cascade_error",
                        model=model,
                        status=response.status_code,
                        error=error_text,
                    )
                    last_error = f"{model}: HTTP {response.status_code} - {error_text}"
                    continue

                # Success — stream from this model
                yield {"type": "model", "model": model}

                total_content = ""
                usage_data = None

                async for line in response.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data_str = line[6:].strip()
                    if data_str == "[DONE]":
                        break

                    try:
                        chunk = json.loads(data_str)
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        content = delta.get("content", "")

                        # Check for usage in the final chunk
                        if chunk.get("usage"):
                            usage_data = chunk["usage"]

                        if content:
                            total_content += content
                            yield {"type": "chunk", "content": content}

                    except json.JSONDecodeError:
                        continue

                # Calculate cost
                input_tokens = usage_data.get("prompt_tokens", 0) if usage_data else 0
                output_tokens = usage_data.get("completion_tokens", 0) if usage_data else 0
                pricing = MODEL_PRICING.get(model, {"input": 0.50, "output": 1.00})
                cost = (input_tokens / 1_000_000) * pricing["input"] + \
                       (output_tokens / 1_000_000) * pricing["output"]

                log.info(
                    "groq_cascade_success",
                    model=model,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    cost_usd=round(cost, 6),
                    content_length=len(total_content),
                )

                yield {
                    "type": "done",
                    "model": model,
                    "usage": {
                        "input_tokens": input_tokens,
                        "output_tokens": output_tokens,
                        "total_tokens": input_tokens + output_tokens,
                    },
                    "cost_usd": round(cost, 6),
                }
                return  # Success — exit cascade

        except httpx.TimeoutException:
            log.warning("groq_cascade_timeout", model=model)
            last_error = f"{model}: timeout"
            continue
        except Exception as e:
            log.error("groq_cascade_exception", model=model, error=str(e))
            last_error = f"{model}: {str(e)}"
            continue

    # All models failed
    log.error("groq_cascade_all_failed", last_error=last_error)
    yield {
        "type": "error",
        "message": f"All AI models are currently unavailable. Last error: {last_error}. Please try again in a few minutes.",
    }


async def non_streaming_groq(
    system_prompt: str,
    user_prompt: str,
    max_tokens: int = 4096,
    temperature: float = 0.7,
) -> dict:
    """
    Non-streaming version — returns the full response at once.
    Used for testing and simpler integrations.
    """
    full_content = ""
    result = {}

    async for event in stream_groq_response(system_prompt, user_prompt, max_tokens, temperature):
        if event["type"] == "chunk":
            full_content += event["content"]
        elif event["type"] == "done":
            result = event
        elif event["type"] == "error":
            return {"error": event["message"]}

    result["content"] = full_content
    return result


# Human-readable model names for the frontend
MODEL_DISPLAY_NAMES = {
    "openai/gpt-oss-120b": "GPT-OSS 120B",
    "openai/gpt-oss-20b": "GPT-OSS 20B",
    "qwen/qwen3-32b": "Qwen 3 32B",
    "llama-3.3-70b-versatile": "Llama 3.3 70B",
    "groq/compound": "Groq Compound AI",
}


def get_model_display_name(model_id: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_id, model_id)
