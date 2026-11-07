"""
Exercise: Hub-and-Spoke Orchestrator
Day: 07 | Domain: D1 + D2
API Required: No

Build the coordinator that delegates customer support requests to
specialized subagents with scoped tool sets.

Instructions:
1. Implement `classify_request` that categorizes customer requests
2. Implement `get_scoped_tools` that returns the right tool subset per category
3. Implement `build_subagent_prompt` that creates structured context for subagents
4. Implement `orchestrate` that ties it all together

Hints:
- Request categories: "inquiry" (read-only), "refund" (needs refund tools),
  "escalation" (needs escalation tools), "general" (basic tools)
- Each category gets different tools -- inquiry agents don't need process_refund
- Subagent prompts must include all context (customer info, request details)
  because subagents start with empty context
- The orchestrator routes communication -- subagents never talk to each other
"""

from typing import Any

# These would be imported from the other exercise files
# from tools import get_tool_definitions
# from agent_loop import run_agent_loop


# Request categories and their tool mappings
REQUEST_CATEGORIES = ["inquiry", "refund", "escalation", "general"]


def classify_request(customer_message: str) -> str:
    """
    Classify a customer request into a handling category.

    Args:
        customer_message: The customer's message text

    Returns:
        One of: "inquiry", "refund", "escalation", "general"
    """
    raise NotImplementedError("Complete this exercise")


def get_scoped_tools(category: str) -> list[str]:
    """
    Return the tool names appropriate for handling this request category.

    Each category gets a minimal, non-overlapping tool set:
    - inquiry: tools for looking up information (read-only)
    - refund: tools for processing refunds (includes prerequisite tools)
    - escalation: tools for handing off to humans
    - general: basic tools for simple responses

    Args:
        category: Request category from classify_request

    Returns:
        List of tool names (strings) for this category
    """
    raise NotImplementedError("Complete this exercise")


def build_subagent_prompt(
    category: str,
    customer_message: str,
    customer_context: dict | None = None,
) -> str:
    """
    Build the structured prompt for a subagent handling this request.

    The subagent starts with an empty context window -- everything it needs
    must be in this prompt string.

    Args:
        category: Request category
        customer_message: The customer's original message
        customer_context: Optional dict with known customer info
            (e.g., {"name": "...", "tier": "...", "account_status": "..."})

    Returns:
        Structured prompt string for the subagent
    """
    raise NotImplementedError("Complete this exercise")


def orchestrate(customer_message: str, customer_context: dict | None = None) -> dict:
    """
    Main orchestration entry point.

    1. Classify the request
    2. Get scoped tools for the category
    3. Build the subagent prompt
    4. Return the orchestration plan (not executing -- no API needed)

    Returns:
        {
            "category": str,
            "tools": list[str],
            "subagent_prompt": str,
        }
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test classify_request
assert classify_request("What's my account balance?") in REQUEST_CATEGORIES
assert classify_request("I want a refund for order #123") == "refund"
assert classify_request("Let me talk to a manager") == "escalation"

# Test get_scoped_tools
inquiry_tools = get_scoped_tools("inquiry")
assert isinstance(inquiry_tools, list), "Must return a list"
assert len(inquiry_tools) >= 1, "Must have at least 1 tool"
assert len(inquiry_tools) <= 5, "Max 5 tools per category"
assert "process_refund" not in inquiry_tools, "Inquiry agents should not have process_refund"

refund_tools = get_scoped_tools("refund")
assert "get_customer" in refund_tools, "Refund agents need get_customer (prerequisite)"
assert "process_refund" in refund_tools, "Refund agents need process_refund"

# Test build_subagent_prompt
prompt = build_subagent_prompt(
    category="refund",
    customer_message="I want a refund for order #456",
    customer_context={"name": "Jane Doe", "tier": "premium"},
)
assert isinstance(prompt, str), "Must return a string"
assert len(prompt) > 50, "Prompt too short"
assert "refund" in prompt.lower(), "Prompt should mention the request context"

# Test orchestrate
result = orchestrate("I want a refund for order #789")
assert "category" in result, "Must return category"
assert "tools" in result, "Must return tools"
assert "subagent_prompt" in result, "Must return subagent_prompt"
assert result["category"] == "refund"

print("All structural checks passed.")
