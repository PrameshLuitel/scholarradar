"""
Agent Runner — Orchestrates multi-pass tool-calling conversations with Groq.
Bridges LLM tool_calls to local Python function execution from the Skolr toolkit.
"""

from __future__ import annotations

import json
from typing import AsyncGenerator, List, Dict, Any

import structlog
from src.utils.groq_cascade import stream_groq_response
from src.mcp_server.tools import get_tool_map, get_openai_tool_definitions

log = structlog.get_logger("utils.agent")

class AgentRunner:
    def __init__(self, system_prompt: str, max_iterations: int = 5):
        self.system_prompt = system_prompt
        self.max_iterations = max_iterations
        self.messages: List[Dict[str, Any]] = [
            {"role": "system", "content": system_prompt}
        ]
        self.tools = get_openai_tool_definitions()
        self.tool_map = get_tool_map()

    async def run(self, user_prompt: str) -> AsyncGenerator[dict, None]:
        """
        Execute the agentic loop.
        Yields chunks and status updates until completion.
        """
        self.messages.append({"role": "user", "content": user_prompt})
        
        for iteration in range(self.max_iterations):
            log.info("agent_iteration_start", iteration=iteration + 1)
            
            # 1. Call LLM
            current_tool_calls = []
            final_chunk_yielded = False
            
            async for event in stream_groq_response(
                system_prompt=self.system_prompt,
                user_prompt=user_prompt,
                messages=self.messages,
                tools=self.tools,
            ):
                if event["type"] == "model":
                    yield event
                elif event["type"] == "chunk":
                    yield event
                elif event["type"] == "tool_call":
                    # Collect tool call deltas
                    # Note: Simplified aggregation for experimental phase
                    current_tool_calls.extend(event["tool_calls"])
                elif event["type"] == "done":
                    # Store the model's message in history
                    # We reconstruct the tool_calls list from the collected deltas
                    full_response = event.get("content", "")
                    msg = {"role": "assistant", "content": full_response}
                    
                    if current_tool_calls:
                        # Reconstruct formal tool_calls list
                        agg_calls = {}
                        for tc in current_tool_calls:
                            idx = tc.get("index", 0)
                            if idx not in agg_calls:
                                agg_calls[idx] = {"id": None, "type": "function", "function": {"name": "", "arguments": ""}}
                            
                            if tc.get("id"):
                                agg_calls[idx]["id"] = tc["id"]
                            
                            fn = tc.get("function", {})
                            if fn.get("name"):
                                agg_calls[idx]["function"]["name"] = fn["name"]
                            if fn.get("arguments"):
                                agg_calls[idx]["function"]["arguments"] += fn["arguments"]
                        
                        msg["tool_calls"] = [v for v in agg_calls.values() if v.get("id")]
                    
                    self.messages.append(msg)
                    final_chunk_yielded = True
                    # If no tools were called, we are done
                    if not current_tool_calls:
                        yield event
                        return

            if not current_tool_calls:
                break
                
            # 2. Execute Tools
            for tc in msg.get("tool_calls", []):
                call_id = tc.get("id")
                func_name = tc.get("function", {}).get("name")
                args_str = tc.get("function", {}).get("arguments", "{}")
                
                log.info("agent_executing_tool", tool=func_name, call_id=call_id)
                yield {"type": "status", "message": f"Thinking... executing {func_name}"}
                
                try:
                    args = json.loads(args_str)
                    func = self.tool_map.get(func_name)
                    
                    if not func:
                        result = f"Error: Tool '{func_name}' not found."
                    else:
                        # Handle both sync and async tools
                        import asyncio
                        if asyncio.iscoroutinefunction(func):
                            result_data = await func(**args)
                        else:
                            result_data = func(**args)
                        result = json.dumps(result_data)
                        
                except Exception as e:
                    log.error("agent_tool_execution_failed", tool=func_name, error=str(e))
                    result = f"Error executing tool: {str(e)}"
                
                self.messages.append({
                    "role": "tool",
                    "tool_call_id": call_id,
                    "name": func_name,
                    "content": result
                })

        # Final safety yield if we hit max iterations
        yield {"type": "error", "message": "Maximum reasoning steps reached."}
