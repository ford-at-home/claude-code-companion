"""
Exercise: Synthesis Agent
Day: 19 | Domain: D5 (Context Management and Reliability)
API Required: No

Build the synthesis agent for the research pipeline. This agent takes analyzed
claims and produces a final report with citations. It uses the case facts pattern
to preserve numerical data during progressive synthesis.

Key concepts exercised:
- Case facts pattern for preserving numerical data
- Progressive synthesis (don't summarize away specifics)
- Citation formatting with source references
- Structured report output

Instructions:
1. Implement `create_synthesis_agent` returning an agent config dict
2. Implement `build_case_facts_from_claims` to extract preservable numerical data
3. Implement `format_report_section` to produce a cited section of the report

Hints:
- The case facts pattern (from Day 15) prevents compaction from destroying
  numbers like "$136.1M" -> "significant revenue"
- Every numerical claim in the report must have a citation
- Progressive synthesis means building the report section by section,
  not summarizing everything at once (which loses specifics)
"""

from typing import Any, Optional


def create_synthesis_agent() -> dict:
    """
    Create the synthesis agent configuration.

    Returns a dict with:
        - name: str
        - description: str
        - tools: list[str] (scoped to synthesis operations)
        - system_prompt: str

    Tools must include ONLY:
        - get_findings
        - write_section
        - add_citation
        - format_report
    """
    raise NotImplementedError("Complete this exercise")


def build_case_facts_from_claims(claims: list[dict]) -> str:
    """
    Extract a case facts block from analyzed claims, preserving all
    numerical values that progressive summarization would destroy.

    Args:
        claims: List of claim dicts from the analysis agent, each with:
            - claim: str
            - source_ref: str
            - confidence: float
            - quote: str
            - category: str

    Returns:
        A structured string containing all numerical values, dates,
        percentages, and their source references. This block survives
        compaction and gets re-injected to preserve specifics.
    """
    raise NotImplementedError("Complete this exercise")


def format_report_section(
    section_title: str,
    claims: list[dict],
    conflicts: list[dict],
) -> str:
    """
    Format a single section of the research report with inline citations.

    Args:
        section_title: The section heading
        claims: Relevant claims for this section (with source_ref)
        conflicts: Any conflicts relevant to this section

    Returns:
        A formatted string containing:
        - Section heading
        - Prose paragraphs with inline citations (e.g., "grew by 23% [1]")
        - A conflict note if sources disagree
        - A confidence summary for the section
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test create_synthesis_agent
agent = create_synthesis_agent()
assert isinstance(agent, dict), "Agent must be a dict"
assert "name" in agent
assert "tools" in agent

allowed_tools = {"get_findings", "write_section", "add_citation", "format_report"}
assert set(agent["tools"]) == allowed_tools, \
    f"Tools must be exactly {allowed_tools}, got {set(agent['tools'])}"

# Test build_case_facts_from_claims
test_claims = [
    {
        "claim": "Renewable energy grew by 23% year-over-year",
        "source_ref": "[1]",
        "confidence": 0.9,
        "quote": "renewable energy capacity grew by 23% year-over-year",
        "category": "statistic",
    },
    {
        "claim": "Total installed capacity reached 450 GW",
        "source_ref": "[1]",
        "confidence": 0.85,
        "quote": "reaching 450 GW total installed capacity",
        "category": "statistic",
    },
    {
        "claim": "Initial projections estimated 18% growth",
        "source_ref": "[1]",
        "confidence": 0.8,
        "quote": "initial projections of 18% growth",
        "category": "statistic",
    },
]

case_facts = build_case_facts_from_claims(test_claims)
assert isinstance(case_facts, str), "Must return a string"
assert "23%" in case_facts, "Must preserve 23% figure"
assert "450" in case_facts, "Must preserve 450 GW figure"
assert "18%" in case_facts, "Must preserve 18% figure"
assert "[1]" in case_facts, "Must preserve source references"
assert len(case_facts) > 100, "Case facts must have real structure"

# Test format_report_section
test_conflicts = [
    {
        "topic": "renewable energy growth rate",
        "claims": [
            {"claim": "grew by 23%", "source_ref": "[1]"},
            {"claim": "grew by approximately 20%", "source_ref": "[2]"},
        ],
        "severity": "different_magnitude",
        "resolution_note": "Difference may be due to measurement methodology",
    },
]

section = format_report_section("Growth Trends", test_claims, test_conflicts)
assert isinstance(section, str), "Must return a string"
assert "Growth Trends" in section, "Must contain section title"
assert "[1]" in section, "Must contain inline citations"
assert "23%" in section, "Must preserve numerical values in report"
assert len(section) > 150, "Section must have real content"

print("All checks passed.")
