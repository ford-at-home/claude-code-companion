"""
Exercise: Error Response Design
Day: 06 | Domain: D2
API Required: No

Design three different error responses for a `get_customer` tool that
demonstrate the critical distinction between access failures and valid
empty results.

Instructions:
1. Implement `build_error_responses` returning three MCP CallToolResult dicts
2. Scenario A: Customer not found (valid query, no matching record)
3. Scenario B: Database timeout (transient infrastructure failure)
4. Scenario C: Access denied (permission/authorization failure)
5. Each response must have correct `isError` value and descriptive content
6. Error messages should include recovery guidance

Hints:
- "Not found" is NOT an error — the tool worked correctly, the answer is "nothing"
- Timeout IS an error — the tool failed to complete its operation
- Access denied IS an error — the tool was blocked from doing its job
- Recovery guidance tells the LLM what to do next (retry, try different params, escalate)
"""


def build_error_responses() -> dict[str, dict]:
    """
    Build three MCP-style error responses for get_customer.

    Returns:
        Dict with keys "not_found", "timeout", "access_denied", each containing:
        {
            "isError": bool,
            "content": [{"type": "text", "text": str}]
        }
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

responses = build_error_responses()

# Must have all three scenarios
assert set(responses.keys()) == {"not_found", "timeout", "access_denied"}, \
    f"Expected keys: not_found, timeout, access_denied. Got: {set(responses.keys())}"

# Each must have correct structure
for key, resp in responses.items():
    assert "isError" in resp, f"{key} missing 'isError'"
    assert "content" in resp, f"{key} missing 'content'"
    assert isinstance(resp["content"], list), f"{key} content must be a list"
    assert len(resp["content"]) >= 1, f"{key} must have at least one content block"
    assert resp["content"][0]["type"] == "text", f"{key} content must be text type"
    assert len(resp["content"][0]["text"]) > 20, f"{key} message too short -- include recovery guidance"

# Critical: isError values must be correct
assert responses["not_found"]["isError"] is False, \
    "not_found should be isError: false -- it's a valid empty result, not an error"
assert responses["timeout"]["isError"] is True, \
    "timeout should be isError: true -- the tool failed to complete"
assert responses["access_denied"]["isError"] is True, \
    "access_denied should be isError: true -- the tool was blocked"

# Check that messages are descriptive (not just "error" or "not found")
for key, resp in responses.items():
    text = resp["content"][0]["text"]
    assert len(text.split()) >= 10, \
        f"{key} message should be descriptive with recovery guidance (got {len(text.split())} words)"

print("All structural checks passed.")
print(f"  not_found: isError={responses['not_found']['isError']} ✓")
print(f"  timeout: isError={responses['timeout']['isError']} ✓")
print(f"  access_denied: isError={responses['access_denied']['isError']} ✓")
