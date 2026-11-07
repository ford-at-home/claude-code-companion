"""
Exercise: Research Pipeline Coordinator
Day: 19 | Domain: D1 (Agentic Architecture and Orchestration)
API Required: No

Build the coordinator that orchestrates the full research pipeline.
This is the hub in the hub-and-spoke pattern -- it decomposes the topic,
dispatches agents, passes context between phases, and handles errors.

Key concepts exercised:
- Hub-and-spoke orchestration
- Broad topic decomposition (avoid the narrow decomposition anti-pattern)
- Parallel execution where possible
- Structured context passing between agents
- Error handling with resume-not-restart

Instructions:
1. Implement `create_coordinator` returning a coordinator config dict
2. Implement `decompose_topic` to break a topic into research subtopics
3. Implement `build_agent_prompt` to construct context-rich prompts for subagents
4. Implement `handle_phase_error` to manage failures without restarting

Hints:
- Broad decomposition: "AI in healthcare" -> ["diagnostic applications",
  "drug discovery", "clinical trial optimization", "patient monitoring",
  "ethical considerations"] -- not just one narrow angle
- Parallel execution: search subtopics can run simultaneously
- Context passing: the coordinator must serialize search results into a format
  the analysis agent can consume (subagents start with fresh context!)
- Resume from failure: if analysis fails on one source, continue with others
"""

from typing import Any, Optional


def create_coordinator(topic: str) -> dict:
    """
    Create the coordinator configuration for the research pipeline.

    Args:
        topic: The research topic to investigate

    Returns a dict with:
        - topic: str (the research topic)
        - agents: list[str] (names of agents to orchestrate)
        - execution_plan: list[dict] (phases with parallel/sequential execution)
        - error_strategy: str ("resume" -- never restart from scratch)
        - system_prompt: str
    """
    raise NotImplementedError("Complete this exercise")


def decompose_topic(topic: str) -> list[str]:
    """
    Decompose a research topic into broad subtopics for parallel investigation.

    Args:
        topic: The main research topic

    Returns:
        List of 4-6 subtopics that cover the topic broadly.

    Anti-pattern to avoid: narrow decomposition.
        BAD:  "AI in healthcare" -> ["AI diagnostics for lung cancer"]
        GOOD: "AI in healthcare" -> ["diagnostic applications", "drug discovery",
               "clinical trial optimization", "patient monitoring",
               "ethical considerations"]

    The subtopics should be:
        - Broad enough to find diverse sources
        - Specific enough to be searchable
        - Non-overlapping where possible
        - Cover multiple angles (technical, social, economic, ethical)
    """
    raise NotImplementedError("Complete this exercise")


def build_agent_prompt(
    agent_name: str,
    phase_context: dict,
) -> str:
    """
    Build a context-rich prompt for a subagent.

    Subagents start with FRESH context -- they do not inherit the coordinator's
    conversation history. Everything the subagent needs must be in this prompt.

    Args:
        agent_name: Which agent to prompt ("search", "analysis", "synthesis")
        phase_context: dict containing results from previous phases:
            For search: {"topic": str, "subtopics": list[str]}
            For analysis: {"sources": list[dict], "topic": str}
            For synthesis: {"claims": list[dict], "conflicts": list[dict],
                           "case_facts": str, "topic": str}

    Returns:
        A complete prompt string containing all context the subagent needs.
    """
    raise NotImplementedError("Complete this exercise")


def handle_phase_error(
    phase: str,
    error: str,
    completed_work: dict,
) -> dict:
    """
    Handle a phase error with resume-not-restart strategy.

    Args:
        phase: Which phase failed ("search", "analysis", "synthesis")
        error: Error description
        completed_work: What was accomplished before the failure

    Returns:
        dict with:
            - strategy: str ("resume" | "skip_and_continue" | "escalate")
            - resume_context: dict (state to pass to the retry)
            - message: str (human-readable explanation)

    Rules:
        - Never restart from scratch
        - If search fails for one subtopic, continue with others
        - If analysis fails for one source, continue with others
        - If synthesis fails, resume from the last completed section
        - Escalate only if ALL subtopics/sources failed
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test create_coordinator
coord = create_coordinator("AI in healthcare")
assert isinstance(coord, dict), "Coordinator must be a dict"
assert coord["topic"] == "AI in healthcare"
assert "agents" in coord
assert "execution_plan" in coord
assert coord["error_strategy"] == "resume", \
    f"Error strategy must be 'resume', got '{coord['error_strategy']}'"

# Test decompose_topic -- must be broad, not narrow
subtopics = decompose_topic("AI in healthcare")
assert isinstance(subtopics, list), "Must return a list"
assert 4 <= len(subtopics) <= 6, \
    f"Expected 4-6 subtopics, got {len(subtopics)}"

# Subtopics should be distinct (no near-duplicates)
for i, t1 in enumerate(subtopics):
    for j, t2 in enumerate(subtopics):
        if i != j:
            # Simple overlap check -- subtopics shouldn't be substrings of each other
            assert t1.lower() not in t2.lower(), \
                f"Subtopics overlap: '{t1}' is contained in '{t2}'"

# Test build_agent_prompt -- search phase
search_prompt = build_agent_prompt("search", {
    "topic": "AI in healthcare",
    "subtopics": ["diagnostic applications", "drug discovery"],
})
assert isinstance(search_prompt, str)
assert "AI in healthcare" in search_prompt, "Must include the topic"
assert "diagnostic" in search_prompt.lower(), "Must include subtopics"
assert len(search_prompt) > 100, "Prompt must be substantive"

# Test build_agent_prompt -- analysis phase (must include source data)
analysis_prompt = build_agent_prompt("analysis", {
    "sources": [
        {"url": "https://example.com/a", "title": "Study A", "snippet": "..."},
    ],
    "topic": "AI in healthcare",
})
assert "example.com" in analysis_prompt or "Study A" in analysis_prompt, \
    "Analysis prompt must include source data (subagent context is fresh!)"

# Test handle_phase_error -- partial search failure
error_result = handle_phase_error(
    phase="search",
    error="Timeout on subtopic 'drug discovery'",
    completed_work={"successful_subtopics": ["diagnostic applications", "patient monitoring"]},
)
assert error_result["strategy"] in ("resume", "skip_and_continue"), \
    f"Partial failure should resume or skip, got '{error_result['strategy']}'"
assert "resume_context" in error_result

# Test handle_phase_error -- total failure should escalate
error_result = handle_phase_error(
    phase="search",
    error="All searches failed",
    completed_work={"successful_subtopics": []},
)
assert error_result["strategy"] == "escalate", \
    f"Total failure should escalate, got '{error_result['strategy']}'"

print("All checks passed.")
