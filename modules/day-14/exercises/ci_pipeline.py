"""
Exercise: CI Pipeline Command Builder
Day: 14 | Domain: D3 + D4
API Required: No

You are building the CI component of the claims-platform monorepo setup.
The function generates the claude -p command that runs in GitHub Actions
for automated PR review.

Instructions:
1. Implement `build_ci_command` that takes a PR number and review type
2. The command must include:
   - -p flag (non-interactive mode)
   - --output-format json (machine-readable output)
   - --json-schema with a review findings schema
   - --allowedTools scoped to read-only operations
   - --max-turns as a safety backstop
3. Handle two review types:
   - "security": focused on vulnerabilities, uses stricter tool scoping
   - "style": focused on code quality and conventions
4. Return the complete command as a string

Hints:
- The command should pipe gh pr diff into claude -p
- Security reviews might need different --max-turns than style reviews
- The --json-schema should match the review type's output needs
- Think about what --append-system-prompt adds for each review type
"""


def build_ci_command(pr_number: int, review_type: str) -> str:
    """
    Generate a claude -p command for CI-based PR review.

    Args:
        pr_number: The pull request number to review
        review_type: Either "security" or "style"

    Returns:
        A complete shell command string ready for CI execution
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test security review
security_cmd = build_ci_command(42, "security")
assert isinstance(security_cmd, str), f"Expected str, got {type(security_cmd)}"
assert "-p" in security_cmd, "Must include -p flag for non-interactive mode"
assert "--output-format" in security_cmd and "json" in security_cmd, \
    "Must include --output-format json"
assert "--max-turns" in security_cmd, "Must include --max-turns safety backstop"
assert "--allowedTools" in security_cmd or "--allowed-tools" in security_cmd, \
    "Must include --allowedTools for tool scoping"
assert "42" in security_cmd, "Must reference the PR number"
assert "security" in security_cmd.lower(), \
    "Security review should reference security context"

# Test style review
style_cmd = build_ci_command(99, "style")
assert "99" in style_cmd, "Must reference the PR number"
assert "-p" in style_cmd, "Must include -p flag"
assert "style" in style_cmd.lower() or "quality" in style_cmd.lower() or "convention" in style_cmd.lower(), \
    "Style review should reference style/quality context"

# Verify the two commands are different
assert security_cmd != style_cmd, "Security and style commands should differ"

print("All structural checks passed.")
