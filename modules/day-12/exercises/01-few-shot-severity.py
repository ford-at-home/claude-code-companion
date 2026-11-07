"""
Exercise: Few-Shot Severity Classification
Day: 12 | Domain: D4
API Required: No

You are building a code review system that classifies findings by severity.
The system needs few-shot examples to teach Claude the severity boundaries --
what's critical, what's minor, and what should be SKIPPED entirely.

Instructions:
1. Implement `build_severity_examples` that returns a string containing
   3 few-shot examples using <example> tags
2. Include exactly three examples:
   - One CRITICAL severity (security vulnerability, data loss risk)
   - One MINOR severity (style issue, naming convention)
   - One SKIP (false positive that should NOT be flagged)
3. Each example must include:
   - The code snippet being reviewed
   - The severity classification
   - A reasoning chain explaining WHY this classification

Hints:
- The SKIP example is the most important -- it teaches Claude that NOT flagging
  is a valid and expected outcome
- Use <example> tags around each example for format consistency
- The reasoning chain should be explicit: "This is critical BECAUSE..."
- All three examples must follow the same output schema
"""


def build_severity_examples() -> str:
    """
    Build 3 few-shot examples demonstrating severity classification
    for code review findings.

    Returns:
        A string containing 3 examples in <example> tags, each with:
        - code_snippet: the code being reviewed
        - severity: "critical", "minor", or "skip"
        - reasoning: explanation of the classification
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

result = build_severity_examples()
assert isinstance(result, str), f"Expected str, got {type(result)}"

# Verify all three severity levels are present
result_lower = result.lower()
assert "critical" in result_lower, "Must include a CRITICAL severity example"
assert "minor" in result_lower, "Must include a MINOR severity example"
assert "skip" in result_lower, "Must include a SKIP example"

# Verify example tags are used
assert "<example>" in result.lower(), "Must use <example> tags"
assert result.lower().count("<example>") >= 3, "Must have at least 3 <example> tags"

# Verify reasoning is present
assert any(word in result_lower for word in ["because", "reason", "since", "this is"]), \
    "Examples must include reasoning for the classification"

# Verify code snippets are present (should contain code-like content)
assert any(char in result for char in ["def ", "function ", "class ", "=", "import", "var ", "const "]), \
    "Examples must include code snippets"

print("All structural checks passed.")
