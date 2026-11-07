"""
Exercise: PreToolUse Hook Configuration
Day: 04 | Domain: D1
API Required: No

A customer service agent has two critical tools: `get_customer` and
`process_refund`. Business rule: refunds MUST NOT be processed unless
the customer has been verified via `get_customer` first.

A prompt instruction ("Always look up the customer before processing a refund")
works 88% of the time. The remaining 12% costs money. You need 100%.

Instructions:
1. Implement `build_hook_config` that returns the PreToolUse hook configuration
   as a dictionary matching the Claude Code hooks JSON schema
2. Implement `validate_refund_prerequisite` that checks session state to
   determine if `get_customer` has been called
3. Implement `get_hook_decision` that returns the hook's decision
   ("allow" or "block" with a reason)

Hints:
- The hook config needs: event type, tool matcher, hook type, and the command/logic
- Session state tracking is YOUR responsibility -- hooks need something to check against
- The block decision should include a message Claude sees, guiding it to call get_customer
"""

from typing import Any


# Session state -- tracks which tools have been called
# In production, this would be maintained by the agentic harness
session_state: dict[str, Any] = {
    "tools_called": [],  # List of tool names that have been executed
    "customer_verified": False,  # Whether get_customer returned successfully
}


def build_hook_config() -> dict:
    """
    Build the PreToolUse hook configuration for the process_refund gate.

    Returns a dictionary matching the Claude Code hooks configuration schema.
    The hook should:
    - Fire on PreToolUse events
    - Match the process_refund tool specifically
    - Use a command-type hook that runs validation

    Expected structure (fill in the values):
    {
        "hooks": [
            {
                "event": "...",
                "matcher": "...",
                "type": "...",
                "command": "..."
            }
        ]
    }
    """
    raise NotImplementedError("Complete this exercise")


def validate_refund_prerequisite(state: dict[str, Any]) -> bool:
    """
    Check whether the prerequisite for process_refund has been met.

    Args:
        state: Current session state dictionary

    Returns:
        True if get_customer has been called and customer is verified,
        False otherwise
    """
    raise NotImplementedError("Complete this exercise")


def get_hook_decision(state: dict[str, Any]) -> dict:
    """
    Return the hook's decision based on current session state.

    Args:
        state: Current session state dictionary

    Returns:
        A decision dict with:
        - "decision": "allow" or "block"
        - "reason": str (explanation, shown to Claude if blocked)
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test hook config structure
config = build_hook_config()
assert isinstance(config, dict), "Must return a dict"
assert "hooks" in config, "Must have 'hooks' key"
assert len(config["hooks"]) >= 1, "Must have at least one hook"

hook = config["hooks"][0]
assert hook.get("event") == "PreToolUse", "Event must be PreToolUse"
assert "process_refund" in hook.get("matcher", ""), "Matcher must target process_refund"

# Test validation with customer NOT verified
unverified_state = {"tools_called": [], "customer_verified": False}
assert validate_refund_prerequisite(unverified_state) is False

# Test validation with customer verified
verified_state = {"tools_called": ["get_customer"], "customer_verified": True}
assert validate_refund_prerequisite(verified_state) is True

# Test hook decisions
block_decision = get_hook_decision(unverified_state)
assert block_decision["decision"] == "block"
assert len(block_decision.get("reason", "")) > 0, "Block must include a reason"

allow_decision = get_hook_decision(verified_state)
assert allow_decision["decision"] == "allow"

print("All structural checks passed.")
