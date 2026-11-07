"""
Exercise: Case Facts Template Builder
Day: 15 | Domain: D5
API Required: No

You are building a case facts template for a customer support agent that handles
multi-issue sessions. The agent may talk to a customer for 20+ turns across
billing disputes, order tracking, and account changes. Context compaction WILL
happen during these sessions, and when it does, numerical values get destroyed.

Your job: build a structured case facts string that preserves every value
that progressive summarization would otherwise generalize or drop.

Instructions:
1. Implement `build_case_facts` that creates a structured case facts template
2. The template must preserve ALL numerical values (dollar amounts, order numbers)
3. The template must preserve ALL dates and timestamps
4. The template must preserve account status and category for each issue
5. Each issue should be clearly separated with its own section
6. The output should be a single string that could be injected into a prompt
   after compaction to restore critical context

Hints:
- Think about what "$136.1M" becomes after summarization ("significant revenue")
- Think about what "Order #ORD-2026-0847291" becomes ("a recent order")
- The format should be machine-parseable AND human-readable
- Null resolutions mean the issue is still open -- this matters for the agent
"""

from typing import Optional


def build_case_facts(customer_id: str, issues: list[dict]) -> str:
    """
    Build a case facts template for a customer support session.

    Each issue dict contains:
        - issue_id: str (e.g., "ISS-001")
        - category: str (e.g., "billing", "shipping", "account")
        - status: str (e.g., "open", "resolved", "escalated")
        - key_facts: list[str] (e.g., ["Charged $47.99 on 2026-03-15",
                                        "Order #ORD-2026-0847291"])
        - resolution: Optional[str] (None if unresolved)

    Returns:
        A formatted string containing all case facts, structured so that
        no numerical value, date, or status is lost to summarization.

    Example input:
        customer_id = "CUST-29471"
        issues = [
            {
                "issue_id": "ISS-001",
                "category": "billing",
                "status": "open",
                "key_facts": [
                    "Charged $47.99 on 2026-03-15",
                    "Expected charge was $29.99",
                    "Difference of $18.00",
                    "Order #ORD-2026-0847291",
                ],
                "resolution": None,
            },
            {
                "issue_id": "ISS-002",
                "category": "shipping",
                "status": "resolved",
                "key_facts": [
                    "Package shipped 2026-03-10",
                    "Tracking #TRK-88234-US",
                    "Delivered 2026-03-14",
                ],
                "resolution": "Confirmed delivery via tracking",
            },
        ]
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test with the example from the docstring
test_issues = [
    {
        "issue_id": "ISS-001",
        "category": "billing",
        "status": "open",
        "key_facts": [
            "Charged $47.99 on 2026-03-15",
            "Expected charge was $29.99",
            "Difference of $18.00",
            "Order #ORD-2026-0847291",
        ],
        "resolution": None,
    },
    {
        "issue_id": "ISS-002",
        "category": "shipping",
        "status": "resolved",
        "key_facts": [
            "Package shipped 2026-03-10",
            "Tracking #TRK-88234-US",
            "Delivered 2026-03-14",
        ],
        "resolution": "Confirmed delivery via tracking",
    },
]

result = build_case_facts("CUST-29471", test_issues)

# Must be a string
assert isinstance(result, str), f"Expected str, got {type(result)}"

# Must contain ALL numerical values -- these are what compaction destroys
assert "$47.99" in result, "Missing dollar amount $47.99"
assert "$29.99" in result, "Missing dollar amount $29.99"
assert "$18.00" in result, "Missing dollar amount $18.00"
assert "ORD-2026-0847291" in result, "Missing order number"
assert "TRK-88234-US" in result, "Missing tracking number"

# Must contain ALL dates
assert "2026-03-15" in result, "Missing date 2026-03-15"
assert "2026-03-10" in result, "Missing date 2026-03-10"
assert "2026-03-14" in result, "Missing date 2026-03-14"

# Must contain customer ID
assert "CUST-29471" in result, "Missing customer ID"

# Must contain issue IDs
assert "ISS-001" in result, "Missing issue ID ISS-001"
assert "ISS-002" in result, "Missing issue ID ISS-002"

# Must contain statuses
assert "open" in result.lower(), "Missing status 'open'"
assert "resolved" in result.lower(), "Missing status 'resolved'"

# Must contain categories
assert "billing" in result.lower(), "Missing category 'billing'"
assert "shipping" in result.lower(), "Missing category 'shipping'"

# Must indicate unresolved issues clearly
assert result.count("ISS-001") >= 1, "ISS-001 must appear at least once"

# Must not be trivially short (a real template has structure)
assert len(result) > 200, f"Result too short ({len(result)} chars) -- needs real structure"

print("All checks passed.")
