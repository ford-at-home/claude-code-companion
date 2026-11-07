"""
Exercise: Coordinator Prompt Design
Day: 02 | Domain: D1
API Required: No

A coordinator agent needs to delegate research on a broad topic to subagents.
The coordinator prompt should be non-procedural -- it specifies WHAT the
output should be and the quality criteria, but lets subagents decide HOW
to accomplish their tasks.

Instructions:
1. Implement `build_coordinator_prompt` that creates a system prompt for
   the coordinator agent
2. The prompt must define the research GOAL (comprehensive, multi-domain)
3. Include all quality_criteria as explicit evaluation standards
4. Do NOT include procedural steps (e.g., "Step 1: search for...",
   "First, find...", "Then analyze...")
5. The prompt should guide decomposition breadth without dictating method

Hints:
- Think about what makes a coordinator effective: it knows WHAT good looks like,
  but trusts subagents to figure out HOW
- Quality criteria should be checkable by a reviewer, not vague aspirations
- The topic parameter means this must work for any research topic, not just one
"""


def build_coordinator_prompt(topic: str, quality_criteria: list[str]) -> str:
    """
    Build a non-procedural coordinator prompt for multi-agent research.

    Args:
        topic: The research topic (e.g., "AI in creative industries")
        quality_criteria: List of quality standards the output must meet
            (e.g., ["Covers at least 5 distinct sub-domains",
                    "Each domain includes at least 2 concrete examples"])

    Returns:
        A system prompt string for the coordinator agent
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test with sample inputs
test_prompt = build_coordinator_prompt(
    topic="AI in creative industries",
    quality_criteria=[
        "Covers at least 5 distinct sub-domains of the creative industries",
        "Each domain includes at least 2 concrete examples with sources",
        "Addresses both current applications and emerging trends",
        "Includes perspectives from practitioners, not just technology vendors",
    ],
)

# Structural checks
assert isinstance(test_prompt, str), "Must return a string"
assert len(test_prompt) > 100, "Prompt is too short to be useful"
assert "AI in creative industries" in test_prompt, "Must include the topic"

# Check that quality criteria are present
for criterion in [
    "5 distinct sub-domains",
    "concrete examples",
    "emerging trends",
    "practitioners",
]:
    assert criterion.lower() in test_prompt.lower() or any(
        word in test_prompt.lower() for word in criterion.lower().split()[:3]
    ), f"Quality criterion about '{criterion}' should be reflected in the prompt"

# Anti-pattern check: should NOT be procedural
procedural_markers = ["step 1", "step 2", "first,", "then,", "next,", "finally,"]
prompt_lower = test_prompt.lower()
procedural_count = sum(1 for marker in procedural_markers if marker in prompt_lower)
assert procedural_count <= 1, (
    f"Prompt appears procedural (found {procedural_count} step markers). "
    "Coordinator prompts should specify WHAT and criteria, not HOW."
)

print("All structural checks passed.")
