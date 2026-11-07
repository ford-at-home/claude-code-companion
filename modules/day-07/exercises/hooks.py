"""
Exercise: Hook Configuration
Day: 07 | Domain: D1 + D2
API Required: No

Configure two hooks for the customer support agent:
1. PreToolUse hook on process_refund (prerequisite gate)
2. Stop hook for quality gate (ensure issue is addressed)

Instructions:
1. Implement `get_hook_config` returning the hooks configuration dict
2. Implement `check_refund_prerequisite` for the PreToolUse gate
3. Implement `check_quality_gate` for the Stop hook
4. Both functions should return decision dicts with "decision" and "reason"

Hints:
- The PreToolUse hook checks if get_customer was called before process_refund
- The Stop hook checks if the agent's response addresses the customer's issue
- Hook decisions are either "allow" or "block" with a reason string
- Remember: hooks = deterministic enforcement, not probabilistic guidance
"""

from typing import Any


# Session state tracker
class SessionState:
    def __init__(self):
        self.tools_called: list[str] = []
        self.customer_verified: bool = False
        self.issue_addressed: bool = False
        self.response_includes_resolution: bool = False

    def record_tool_call(self, tool_name: str, success: bool = True):
        """Record a tool call in session state."""
        self.tools_called.append(tool_name)
        if tool_name == "get_customer" and success:
            self.customer_verified = True


def get_hook_config() -> dict:
    """
    Return the hooks configuration for the customer support agent.

    Must include:
    1. A PreToolUse hook matching process_refund
    2. A Stop hook for quality gate

    Expected structure:
    {
        "hooks": [
            {"event": "PreToolUse", "matcher": "...", "type": "...", ...},
            {"event": "Stop", "type": "...", ...}
        ]
    }
    """
    raise NotImplementedError("Complete this exercise")


def check_refund_prerequisite(state: SessionState) -> dict:
    """
    PreToolUse decision for process_refund.

    Args:
        state: Current session state

    Returns:
        {"decision": "allow" or "block", "reason": str}
    """
    raise NotImplementedError("Complete this exercise")


def check_quality_gate(state: SessionState, agent_response: str) -> dict:
    """
    Stop hook decision — checks if the agent has adequately addressed
    the customer's issue before allowing it to finish.

    Args:
        state: Current session state
        agent_response: The agent's final response text

    Returns:
        {"decision": "allow" or "block", "reason": str}
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test hook config structure
config = get_hook_config()
assert "hooks" in config, "Must have 'hooks' key"
hooks = config["hooks"]
assert len(hooks) >= 2, "Must have at least 2 hooks"

events = [h["event"] for h in hooks]
assert "PreToolUse" in events, "Must have a PreToolUse hook"
assert "Stop" in events, "Must have a Stop hook"

# Test PreToolUse gate
state_no_customer = SessionState()
block_result = check_refund_prerequisite(state_no_customer)
assert block_result["decision"] == "block", "Should block refund without customer verification"

state_with_customer = SessionState()
state_with_customer.record_tool_call("get_customer", success=True)
allow_result = check_refund_prerequisite(state_with_customer)
assert allow_result["decision"] == "allow", "Should allow refund after customer verification"

# Test Stop quality gate
state_incomplete = SessionState()
block_stop = check_quality_gate(state_incomplete, "I'll look into that.")
assert block_stop["decision"] == "block", "Should block incomplete responses"

state_complete = SessionState()
state_complete.issue_addressed = True
state_complete.response_includes_resolution = True
allow_stop = check_quality_gate(state_complete, "Your refund of $50 has been processed.")
assert allow_stop["decision"] == "allow", "Should allow complete responses"

print("All structural checks passed.")
