"""
Exercise: Tool Definitions
Day: 07 | Domain: D1 + D2
API Required: No

Define four customer support tools with proper descriptions, input schemas,
and response formats. These definitions are used by hooks.py, agent_loop.py,
and orchestrator.py.

Instructions:
1. Implement `get_tool_definitions` returning a list of 4 tool dicts
2. Each tool needs: name, description (3-4 sentences), input_schema
3. Descriptions must clearly state what, when, parameters, and limitations
4. Implement `execute_tool` that dispatches to the correct handler
5. Implement each tool handler with simulated behavior

Hints:
- get_customer returns profile data (name, email, status, tier)
- process_refund requires order_id and amount, returns confirmation
- escalate_to_human requires reason and customer context
- check_policy requires action_type and parameters, returns allowed/denied
"""

from typing import Any


def get_tool_definitions() -> list[dict]:
    """
    Return tool definitions for the customer support agent.

    Each tool dict must have:
    - "name": str
    - "description": str (3-4 sentences covering what/when/params/limits)
    - "input_schema": dict (JSON Schema)
    """
    raise NotImplementedError("Complete this exercise")


def execute_tool(tool_name: str, tool_input: dict[str, Any]) -> dict:
    """
    Execute a tool and return an MCP-style response.

    Returns:
        {
            "isError": bool,
            "content": [{"type": "text", "text": str}]
        }
    """
    raise NotImplementedError("Complete this exercise")


# --- Simulated tool handlers ---

def _handle_get_customer(tool_input: dict) -> dict:
    """Simulate customer lookup."""
    raise NotImplementedError("Complete this exercise")


def _handle_process_refund(tool_input: dict) -> dict:
    """Simulate refund processing."""
    raise NotImplementedError("Complete this exercise")


def _handle_escalate_to_human(tool_input: dict) -> dict:
    """Simulate human escalation."""
    raise NotImplementedError("Complete this exercise")


def _handle_check_policy(tool_input: dict) -> dict:
    """Simulate policy check."""
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

tools = get_tool_definitions()

# Must have exactly 4 tools
assert len(tools) == 4, f"Expected 4 tools, got {len(tools)}"

# Check required tool names
tool_names = {t["name"] for t in tools}
expected = {"get_customer", "process_refund", "escalate_to_human", "check_policy"}
assert tool_names == expected, f"Expected tools: {expected}. Got: {tool_names}"

# Check structure
for tool in tools:
    assert "description" in tool, f"{tool['name']} missing description"
    assert "input_schema" in tool, f"{tool['name']} missing input_schema"
    assert len(tool["description"]) >= 80, \
        f"{tool['name']} description too short — need 3-4 sentences"

# Check execute_tool dispatches correctly
result = execute_tool("get_customer", {"customer_id": "cust-123"})
assert "isError" in result, "execute_tool must return isError field"
assert "content" in result, "execute_tool must return content field"

print("All structural checks passed.")
