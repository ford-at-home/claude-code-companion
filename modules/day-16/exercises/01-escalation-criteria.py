"""
Exercise: Escalation Criteria Builder
Day: 16 | Domain: D5
API Required: No

You are building escalation criteria for a customer support agent. The criteria
must be DETERMINISTIC -- based on concrete conditions, not sentiment analysis.

The prompt you build will be injected into the agent's system prompt to guide
its escalation decisions. It must include:
1. Clear, deterministic escalation criteria (not sentiment-based)
2. Three few-shot examples demonstrating the criteria in action:
   a. One that SHOULD escalate (policy gap)
   b. One that should NOT escalate (frustrated but resolvable)
   c. One edge case (customer says "let me talk to someone" but issue is trivial)

Instructions:
1. Implement `build_escalation_prompt` that returns a complete prompt string
2. Criteria must reference concrete conditions, never emotional tone
3. Each example must include the scenario, the decision, and the reasoning
4. The edge case example is the most important -- it teaches the model nuance

Hints:
- "Customer seems angry" is NOT a valid escalation criterion
- "Customer explicitly requests human AND issue cannot be resolved with available tools"
  IS a valid criterion (note the AND -- both conditions matter)
- The edge case teaches the model that "let me talk to someone" alone is not
  sufficient when the issue is trivially solvable
"""

from typing import Optional


def build_escalation_prompt(
    criteria: list[dict], examples: list[dict]
) -> str:
    """
    Build an escalation criteria prompt with few-shot examples.

    Each criterion dict contains:
        - name: str (e.g., "policy_gap")
        - description: str (e.g., "Situation not covered by available instructions")
        - is_deterministic: bool (must be True for all criteria)

    Each example dict contains:
        - scenario: str (description of the customer interaction)
        - should_escalate: bool
        - reasoning: str (why the decision was made)
        - matching_criteria: list[str] (names of triggered criteria, empty if none)

    Returns:
        A formatted prompt string containing escalation rules and examples.
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test criteria -- all must be deterministic
test_criteria = [
    {
        "name": "explicit_human_request",
        "description": "Customer explicitly asks for a human agent or manager",
        "is_deterministic": True,
    },
    {
        "name": "policy_gap",
        "description": "Situation not covered by available instructions or tools",
        "is_deterministic": True,
    },
    {
        "name": "exhausted_approaches",
        "description": "Agent has tried all available resolution options without success",
        "is_deterministic": True,
    },
    {
        "name": "confidence_threshold",
        "description": "Agent confidence score falls below 70% for the proposed resolution",
        "is_deterministic": True,
    },
]

# Three required examples
test_examples = [
    {
        "scenario": (
            "Customer purchased a product that was recalled after their purchase. "
            "They want a full refund plus compensation for inconvenience. "
            "The refund policy covers returns but says nothing about recalled items "
            "or compensation beyond the purchase price."
        ),
        "should_escalate": True,
        "reasoning": (
            "The recall situation plus compensation request falls outside documented "
            "refund policy. This is a policy gap -- no available instructions cover "
            "recalled product compensation."
        ),
        "matching_criteria": ["policy_gap"],
    },
    {
        "scenario": (
            "Customer is very frustrated because their package arrived 2 days late. "
            "They use strong language and say this is 'unacceptable.' "
            "The order tracking shows the package was delivered. "
            "The agent can offer a courtesy credit per standard policy."
        ),
        "should_escalate": False,
        "reasoning": (
            "Despite the customer's frustration, the issue is resolvable with "
            "available tools. A courtesy credit is within policy. Emotional tone "
            "alone is never an escalation trigger."
        ),
        "matching_criteria": [],
    },
    {
        "scenario": (
            "Customer says 'Just let me talk to a real person.' "
            "Their issue is a simple password reset, which the agent can complete "
            "in one step via the reset_password tool."
        ),
        "should_escalate": False,
        "reasoning": (
            "Although the customer requested a human, the issue is trivially "
            "solvable. The agent should acknowledge the request, explain it can "
            "resolve this immediately, and offer to escalate if the customer "
            "still prefers a human after seeing the solution. An explicit request "
            "alone is not sufficient when the resolution is immediate and certain."
        ),
        "matching_criteria": [],
    },
]

result = build_escalation_prompt(test_criteria, test_examples)

# Must be a string
assert isinstance(result, str), f"Expected str, got {type(result)}"

# Must contain all criteria names
for criterion in test_criteria:
    assert criterion["name"] in result, f"Missing criterion: {criterion['name']}"
    assert criterion["description"] in result, f"Missing description for: {criterion['name']}"

# Must contain all three examples
assert "recalled" in result.lower(), "Missing escalation example (recalled product)"
assert "password reset" in result.lower() or "password" in result.lower(), \
    "Missing edge case example (password reset)"
assert "courtesy credit" in result.lower() or "late" in result.lower(), \
    "Missing non-escalation example (late package)"

# Must contain escalation decisions
assert result.lower().count("escalate") >= 3, \
    "Must reference escalation decisions for all examples"

# Must NOT contain sentiment-based language as criteria
sentiment_words = ["seems angry", "sounds upset", "appears frustrated", "tone of voice"]
for word in sentiment_words:
    assert word not in result.lower(), \
        f"Contains sentiment-based language in criteria: '{word}'"

# Must be substantial
assert len(result) > 500, f"Result too short ({len(result)} chars) -- needs real structure"

print("All checks passed.")
