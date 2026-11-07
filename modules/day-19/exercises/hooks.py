"""
Exercise: Quality Enforcement Hooks
Day: 19 | Domain: D1 (Agentic Architecture) + D4 (Prompt Engineering)
API Required: No

Build the quality enforcement hooks for the research pipeline. Hooks turn
prompt-based suggestions into deterministic enforcement -- they execute every
time, unlike prompt instructions which can be forgotten under context pressure.

Key concepts exercised:
- PreToolUse hooks for prerequisite gates
- Stop hooks for quality verification
- Prompt-type hooks using LLM evaluation
- Explicit criteria (not vague "check quality")

Instructions:
1. Implement `create_hooks` returning a hooks config dict
2. Implement `check_prerequisites` to validate phase ordering
3. Implement `evaluate_report_quality` to score the final report

Hints:
- PreToolUse hook: block synthesis tools if analysis hasn't completed
- Stop hook: verify the report meets completeness, citation, and accuracy criteria
- Quality criteria must be EXPLICIT, not "seems good enough"
"""

from typing import Any, Optional


def create_hooks() -> dict:
    """
    Create the hooks configuration for the research pipeline.

    Returns a dict with:
        - pre_tool_use: list[dict] (hooks that fire before tool execution)
        - stop: list[dict] (hooks that fire when agents finish)

    Each pre_tool_use hook dict contains:
        - name: str
        - blocked_tools: list[str] (tools this hook can block)
        - condition: str (when to block -- e.g., "analysis_not_complete")
        - message: str (error message when blocked)

    Each stop hook dict contains:
        - name: str
        - type: str ("prompt" -- uses LLM evaluation)
        - criteria: list[str] (explicit quality criteria to check)
        - action_on_fail: str ("block" -- forces continued work)
    """
    raise NotImplementedError("Complete this exercise")


def check_prerequisites(
    current_phase: str,
    completed_phases: list[str],
    tool_name: str,
) -> dict:
    """
    Check whether a tool call is allowed given the current pipeline state.

    Args:
        current_phase: The active phase ("search", "analysis", "synthesis")
        completed_phases: List of phases that have completed
        tool_name: The tool being invoked

    Returns:
        dict with:
            - allowed: bool
            - reason: str (why blocked or allowed)

    Rules:
        - Analysis tools require "search" in completed_phases
        - Synthesis tools require "analysis" in completed_phases
        - Search tools are always allowed
    """
    raise NotImplementedError("Complete this exercise")


def evaluate_report_quality(report: dict) -> dict:
    """
    Evaluate whether a research report meets quality criteria.

    Args:
        report: dict with:
            - sections: list[dict] (each with title, content, citations)
            - case_facts: str (preserved numerical data)
            - source_count: int (number of unique sources)
            - claim_count: int (number of extracted claims)

    Returns:
        dict with:
            - passed: bool
            - score: float (0.0 to 1.0)
            - criteria_results: list[dict] (each criterion and its pass/fail)
            - blocking_issues: list[str] (issues that prevent acceptance)

    Criteria (all must pass for overall pass):
        1. completeness: at least 3 sections with content
        2. citation_coverage: every section must have at least 1 citation
        3. source_diversity: at least 2 unique sources referenced
        4. numerical_preservation: case_facts must contain at least 1 number
        5. no_unsupported_claims: claim_count must be > 0
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test create_hooks
hooks = create_hooks()
assert isinstance(hooks, dict), "Hooks must be a dict"
assert "pre_tool_use" in hooks, "Must have pre_tool_use hooks"
assert "stop" in hooks, "Must have stop hooks"
assert len(hooks["pre_tool_use"]) >= 1, "Need at least 1 pre_tool_use hook"
assert len(hooks["stop"]) >= 1, "Need at least 1 stop hook"

# Pre-tool-use hooks must block synthesis before analysis
synth_hook = next(
    (h for h in hooks["pre_tool_use"] if "synthesis" in h.get("name", "").lower()
     or any("write_section" in t or "format_report" in t
            for t in h.get("blocked_tools", []))),
    None
)
assert synth_hook is not None, "Must have a hook blocking synthesis tools"

# Stop hooks must have explicit criteria
stop_hook = hooks["stop"][0]
assert "criteria" in stop_hook, "Stop hook must have criteria"
assert len(stop_hook["criteria"]) >= 3, \
    f"Stop hook needs at least 3 criteria, got {len(stop_hook['criteria'])}"

# Test check_prerequisites -- synthesis blocked before analysis
result = check_prerequisites("synthesis", ["search"], "write_section")
assert not result["allowed"], "Synthesis should be blocked before analysis completes"

# Test check_prerequisites -- synthesis allowed after analysis
result = check_prerequisites("synthesis", ["search", "analysis"], "write_section")
assert result["allowed"], "Synthesis should be allowed after analysis completes"

# Test check_prerequisites -- search always allowed
result = check_prerequisites("search", [], "web_search")
assert result["allowed"], "Search should always be allowed"

# Test evaluate_report_quality -- passing report
good_report = {
    "sections": [
        {"title": "Overview", "content": "Growth reached 23% [1]", "citations": ["[1]"]},
        {"title": "Analysis", "content": "Capacity hit 450 GW [1][2]", "citations": ["[1]", "[2]"]},
        {"title": "Outlook", "content": "Projections suggest 30% [2]", "citations": ["[2]"]},
    ],
    "case_facts": "23%, 450 GW, 18%, 30%",
    "source_count": 3,
    "claim_count": 5,
}
quality = evaluate_report_quality(good_report)
assert quality["passed"], f"Good report should pass, got blocking issues: {quality.get('blocking_issues')}"
assert quality["score"] > 0.8, f"Good report should score > 0.8, got {quality['score']}"

# Test evaluate_report_quality -- failing report (no citations)
bad_report = {
    "sections": [
        {"title": "Overview", "content": "Some stuff happened", "citations": []},
    ],
    "case_facts": "",
    "source_count": 0,
    "claim_count": 0,
}
quality = evaluate_report_quality(bad_report)
assert not quality["passed"], "Bad report should fail"
assert len(quality["blocking_issues"]) >= 2, \
    f"Bad report should have multiple blocking issues, got {len(quality['blocking_issues'])}"

print("All checks passed.")
