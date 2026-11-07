"""
Exercise: Analysis Agent
Day: 19 | Domain: D4 (Prompt Engineering and Structured Output)
API Required: No

Build the analysis agent for the research pipeline. This agent reads source
documents, extracts claims with confidence scores, and detects conflicts
between sources.

Key concepts exercised:
- Explicit criteria for claim extraction (not vague "find important stuff")
- Structured output with confidence scoring per claim
- Claim-source mapping with numbered references
- Conflicting source detection

Instructions:
1. Implement `create_analysis_agent` returning an agent config dict
2. Implement `extract_claims` to pull structured claims from source text
3. Implement `detect_conflicts` to find contradictions between claims

Hints:
- Each claim needs a source reference (numbered) and confidence score
- Confidence is per-claim, not per-document (field-level, not document-level)
- Conflicting claims: same topic, different conclusions from different sources
"""

from typing import Any, Optional


def create_analysis_agent() -> dict:
    """
    Create the analysis agent configuration.

    Returns a dict with:
        - name: str
        - description: str
        - tools: list[str] (scoped to analysis operations)
        - system_prompt: str

    Tools must include ONLY:
        - read_document
        - extract_claims
        - compare_sources
        - summarize
    """
    raise NotImplementedError("Complete this exercise")


def extract_claims(source_text: str, source_id: str) -> list[dict]:
    """
    Extract structured claims from a source document.

    Args:
        source_text: The full text of the source document
        source_id: A unique identifier for this source (e.g., "[1]")

    Returns:
        List of claim dicts, each containing:
            - claim: str (the factual assertion)
            - source_ref: str (e.g., "[1]")
            - confidence: float (0.0 to 1.0)
            - quote: str (word-for-word excerpt supporting the claim)
            - category: str (e.g., "statistic", "finding", "opinion", "methodology")

    Rules:
        - Every claim must have a direct quote from the source
        - Confidence reflects how explicitly the source states the claim
        - Statistics and direct findings get higher confidence than interpretations
        - If the source doesn't support a claim, don't fabricate one
    """
    raise NotImplementedError("Complete this exercise")


def detect_conflicts(all_claims: list[dict]) -> list[dict]:
    """
    Detect conflicting claims across sources.

    Args:
        all_claims: All extracted claims from all sources

    Returns:
        List of conflict dicts, each containing:
            - topic: str (what the claims are about)
            - claims: list[dict] (the conflicting claims, each with source_ref)
            - severity: str ("direct_contradiction" | "different_magnitude" |
                            "different_timeframe" | "methodological_difference")
            - resolution_note: str (guidance for the synthesis agent)
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test create_analysis_agent
agent = create_analysis_agent()
assert isinstance(agent, dict), "Agent must be a dict"
assert "name" in agent
assert "description" in agent
assert "tools" in agent
assert "system_prompt" in agent

allowed_tools = {"read_document", "extract_claims", "compare_sources", "summarize"}
assert set(agent["tools"]) == allowed_tools, \
    f"Tools must be exactly {allowed_tools}, got {set(agent['tools'])}"

# Test extract_claims
test_source = """
A 2025 study by the National Institute found that renewable energy capacity
grew by 23% year-over-year, reaching 450 GW total installed capacity.
The researchers noted this exceeded their initial projections of 18% growth.
However, some industry analysts suggest the actual figure may be closer to 20%
due to differences in measurement methodology.
"""

claims = extract_claims(test_source.strip(), "[1]")
assert isinstance(claims, list), "Must return a list"
assert len(claims) >= 2, f"Expected at least 2 claims, got {len(claims)}"

for claim in claims:
    assert "claim" in claim, "Each claim must have a 'claim' field"
    assert "source_ref" in claim, "Each claim must have a 'source_ref' field"
    assert claim["source_ref"] == "[1]", f"Source ref must be '[1]', got '{claim['source_ref']}'"
    assert "confidence" in claim, "Each claim must have a 'confidence' field"
    assert 0.0 <= claim["confidence"] <= 1.0, \
        f"Confidence must be 0.0-1.0, got {claim['confidence']}"
    assert "quote" in claim, "Each claim must have a 'quote' field"
    assert "category" in claim, "Each claim must have a 'category' field"

# At least one claim should reference the 23% figure
has_stat = any("23%" in c["claim"] or "23%" in c["quote"] for c in claims)
assert has_stat, "Should extract the 23% growth statistic"

# Test detect_conflicts
test_claims = [
    {
        "claim": "Renewable energy grew by 23% year-over-year",
        "source_ref": "[1]",
        "confidence": 0.9,
        "quote": "renewable energy capacity grew by 23% year-over-year",
        "category": "statistic",
    },
    {
        "claim": "Renewable energy grew by approximately 20% year-over-year",
        "source_ref": "[2]",
        "confidence": 0.75,
        "quote": "the actual figure may be closer to 20%",
        "category": "statistic",
    },
]

conflicts = detect_conflicts(test_claims)
assert isinstance(conflicts, list), "Must return a list"
assert len(conflicts) >= 1, "Should detect at least 1 conflict"

conflict = conflicts[0]
assert "topic" in conflict, "Conflict must have a topic"
assert "claims" in conflict, "Conflict must list the conflicting claims"
assert "severity" in conflict, "Conflict must have a severity"
assert conflict["severity"] in {
    "direct_contradiction", "different_magnitude",
    "different_timeframe", "methodological_difference"
}, f"Invalid severity: {conflict['severity']}"
assert "resolution_note" in conflict, "Conflict must have a resolution_note"

print("All checks passed.")
