"""
Exercise: Review Prompt Template
Day: 14 | Domain: D3 + D4
API Required: No

You are building the prompt template that the CI pipeline feeds to Claude
for PR review. This prompt must use explicit criteria (not "check for issues")
and include few-shot severity examples.

Instructions:
1. Implement `build_review_prompt` that takes a diff string and review type
2. The prompt must include:
   - Explicit review criteria (specific, actionable conditions to check)
   - 3 few-shot examples using <example> tags showing severity classification
   - The diff content embedded in the prompt
   - Output format instructions matching the CI pipeline's json-schema
3. For "security" review type: criteria focused on vulnerabilities
   (SQL injection, hardcoded secrets, auth bypass, etc.)
4. For "style" review type: criteria focused on code quality and conventions
   (naming, documentation, error handling patterns, etc.)

Hints:
- "Flag issues" is vague. "Flag when user input is passed to SQL without
  parameterization" is explicit.
- The few-shot examples should include a SKIP case (false positive)
- The diff is the primary input -- make sure Claude knows to analyze it
- Output format should match what the CI pipeline's --json-schema expects
"""


def build_review_prompt(diff: str, review_type: str) -> str:
    """
    Build a review prompt with explicit criteria and few-shot examples.

    Args:
        diff: The PR diff content to review
        review_type: Either "security" or "style"

    Returns:
        A complete prompt string with criteria, examples, and the diff
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

sample_diff = """
diff --git a/backend/api/routes/claims.py b/backend/api/routes/claims.py
--- a/backend/api/routes/claims.py
+++ b/backend/api/routes/claims.py
@@ -10,6 +10,15 @@ from models import Claim
+@router.post("/claims/search")
+async def search_claims(query: str):
+    sql = f"SELECT * FROM claims WHERE description LIKE '%{query}%'"
+    results = await db.execute(sql)
+    return {"claims": results}
"""

# Test security review
security_prompt = build_review_prompt(sample_diff, "security")
assert isinstance(security_prompt, str), f"Expected str, got {type(security_prompt)}"
assert len(security_prompt) > 200, "Prompt seems too short for criteria + examples"

# Verify explicit criteria (not vague)
security_lower = security_prompt.lower()
assert any(term in security_lower for term in ["sql", "injection", "parameteriz", "secret", "credential", "auth"]), \
    "Security prompt must include specific security criteria"

# Verify few-shot examples
assert "<example>" in security_prompt, "Must include <example> tags for few-shot examples"
assert security_prompt.count("<example>") >= 3, "Must have at least 3 few-shot examples"

# Verify diff is included
assert "claims" in security_prompt, "The diff content must be embedded in the prompt"

# Verify skip case exists
assert "skip" in security_lower or "false positive" in security_lower or "not a finding" in security_lower, \
    "Must include a skip/false-positive example"

# Test style review
style_prompt = build_review_prompt(sample_diff, "style")
style_lower = style_prompt.lower()
assert any(term in style_lower for term in ["naming", "convention", "readab", "document", "docstring", "type"]), \
    "Style prompt must include specific style/quality criteria"

# Verify both reviews include the diff
assert sample_diff.strip()[:50] in security_prompt or "claims" in security_prompt, \
    "Security prompt must include the diff"

print("All structural checks passed.")
