"""
Tool registry — auto-discovers and registers all tool modules in this package.

Each tool file must export a `register_tools(mcp)` function that registers
its tools with the FastMCP instance using the `@mcp.tool()` decorator.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict, List

import structlog

if TYPE_CHECKING:
    from mcp.server.fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools")

# Modules to skip during auto-discovery
_SKIP_MODULES = {"__init__"}


def discover_tool_modules() -> list[str]:
    """Return a list of importable module names in this package."""
    package_dir = Path(__file__).parent
    modules: list[str] = []
    for info in pkgutil.iter_modules([str(package_dir)]):
        if info.name not in _SKIP_MODULES:
            modules.append(info.name)
    return sorted(modules)


def register_all_tools(mcp: "FastMCP") -> list[str]:
    """Discover and register all tools from this package."""
    loaded: list[str] = []
    for module_name in discover_tool_modules():
        fqn = f"src.mcp_server.tools.{module_name}"
        try:
            mod = importlib.import_module(fqn)
            register_fn = getattr(mod, "register_tools", None)
            if register_fn is None:
                continue
            register_fn(mcp)
            loaded.append(module_name)
        except Exception as e:
            log.error("tool_module_load_failed", module=module_name, error=str(e))
    return loaded


def get_tool_map() -> Dict[str, Callable]:
    """
    Return a map of tool names to their implementation functions.
    Used for native LLM tool execution.
    """
    tool_map: Dict[str, Callable] = {}
    from fastmcp import FastMCP
    temp_mcp = FastMCP("ToolDiscovery")
    
    for module_name in discover_tool_modules():
        fqn = f"src.mcp_server.tools.{module_name}"
        try:
            mod = importlib.import_module(fqn)
            register_fn = getattr(mod, "register_tools", None)
            if register_fn:
                register_fn(temp_mcp)
        except Exception as e:
            log.error("tool_map_load_failed", module=module_name, error=str(e))
            
    # Extract from FastMCP's internal registry
    for name, tool in temp_mcp._tool_manager.list_tools():
        tool_map[name] = tool.fn
    return tool_map


def get_openai_tool_definitions() -> List[dict]:
    """
    Return tool definitions in OpenAI/Groq format.
    """
    from fastmcp import FastMCP
    temp_mcp = FastMCP("Definitions")
    register_all_tools(temp_mcp)
    
    openai_tools = []
    for name, tool in temp_mcp._tool_manager.list_tools():
        # FastMCP uses pydantic/inspect to generate descriptions
        # We manually build a simplified version here for compatibility
        sig = inspect.signature(tool.fn)
        params = {
            "type": "object",
            "properties": {},
            "required": []
        }
        
        for param_name, param in sig.parameters.items():
            if param_name == "self": continue
            
            p_info = {"type": "string"} # Default
            if param.annotation == int: p_info["type"] = "integer"
            elif param.annotation == float: p_info["type"] = "number"
            elif param.annotation == bool: p_info["type"] = "boolean"
            
            # Extract docstring info for parameter description if possible
            # (Simplified: FastMCP handles this better but we need it as a dict)
            params["properties"][param_name] = p_info
            if param.default == inspect.Parameter.empty:
                params["required"].append(param_name)
        
        openai_tools.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool.description or f"Execute {name}",
                "parameters": params
            }
        })
    return openai_tools
