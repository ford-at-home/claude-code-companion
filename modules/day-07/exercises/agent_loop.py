"""
Exercise: Agentic Loop with Error Recovery
Day: 07 | Domain: D1 + D2
API Required: No

Build the canonical agentic loop for the customer support agent.
This loop integrates tool execution (from tools.py), hook checking
(from hooks.py), and proper error recovery.

Instructions:
1. Implement `run_agent_loop` with correct stop_reason branching
2. Before executing a tool, check hooks via `check_hooks`
3. Handle tool execution errors using isError patterns
4. Include safety backstop (max iterations) as backup, not primary control
5. Return the final response text when stop_reason == "end_turn"

Hints:
- The loop must handle: tool_use, end_turn, pause_turn, and error cases
- Hook checks happen BEFORE tool execution (PreToolUse)
- If a hook blocks, append the block reason as a tool_result error
- Tool execution errors (isError: true) should be appended as tool_results
  so Claude can see and recover from them
"""

from typing import Any

# These would be imported from the other exercise files in a real system
# from tools import execute_tool
# from hooks import check_refund_prerequisite, SessionState


MAX_ITERATIONS = 30


def check_hooks(tool_name: str, session_state: Any) -> dict:
    """
    Check if any hooks should block this tool call.

    Args:
        tool_name: Name of the tool about to be executed
        session_state: Current session state

    Returns:
        {"allowed": True} or {"allowed": False, "reason": str}
    """
    raise NotImplementedError("Complete this exercise")


def run_agent_loop(
    client: Any,
    messages: list[dict],
    tools: list[dict],
    session_state: Any,
) -> str:
    """
    Run the agentic loop with hook checking and error recovery.

    Args:
        client: Anthropic API client (or mock)
        messages: Initial conversation messages
        tools: Tool definitions
        session_state: Mutable session state for hook tracking

    Returns:
        Claude's final text response
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

import inspect

# Verify function signatures
sig = inspect.signature(run_agent_loop)
params = list(sig.parameters.keys())
assert params == ["client", "messages", "tools", "session_state"], \
    f"Expected params [client, messages, tools, session_state], got {params}"

sig_hooks = inspect.signature(check_hooks)
params_hooks = list(sig_hooks.parameters.keys())
assert params_hooks == ["tool_name", "session_state"], \
    f"Expected params [tool_name, session_state], got {params_hooks}"

# Verify check_hooks returns correct structure
# (This requires the function to be implemented)
try:
    hook_result = check_hooks("get_customer", None)
    assert "allowed" in hook_result, "check_hooks must return dict with 'allowed' key"
except NotImplementedError:
    pass  # OK if not yet implemented

print("All structural checks passed.")
