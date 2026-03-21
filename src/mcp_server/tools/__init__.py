"""
Tool registry — auto-discovers and registers all tool modules in this package.

Each tool file must export a `register_tools(mcp)` function that registers
its tools with the FastMCP instance using the `@mcp.tool()` decorator.
"""

from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path
from typing import TYPE_CHECKING

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
    """
    Discover and register all tools from this package.

    Returns a list of successfully loaded module names.
    """
    loaded: list[str] = []
    for module_name in discover_tool_modules():
        fqn = f"src.mcp_server.tools.{module_name}"
        try:
            mod = importlib.import_module(fqn)
            register_fn = getattr(mod, "register_tools", None)
            if register_fn is None:
                log.warning("tool_module_missing_register", module=module_name)
                continue
            register_fn(mcp)
            loaded.append(module_name)
            log.info("tool_module_registered", module=module_name)
        except Exception as e:
            log.error("tool_module_load_failed", module=module_name, error=str(e))
    log.info("tool_registry_complete", loaded_count=len(loaded), modules=loaded)
    return loaded
