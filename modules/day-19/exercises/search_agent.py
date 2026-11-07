"""
Exercise: Search Agent
Day: 19 | Domain: D2 (Tool Design and MCP Integration)
API Required: No

Build the search agent for the research pipeline. This agent finds sources
on a given topic using scoped tools and returns deduplicated results with
metadata.

Key concepts exercised:
- Scoped tool sets (only search-relevant tools)
- isError distinction (access failure vs. valid empty results)
- Result deduplication
- Source metadata preservation

Instructions:
1. Implement `create_search_agent` returning an agent config dict
2. Implement `deduplicate_results` to remove duplicate sources by URL
3. Implement `handle_search_error` to distinguish access failures from empty results

Hints:
- The agent should have ONLY search-relevant tools (web_search, academic_search,
  news_search, bookmark_result) -- scoped access, not everything
- isError: true means the search FAILED (network error, permission denied)
- isError: false with empty results means the search WORKED but found nothing
- These two cases require different handling: retry vs. move on
"""

from typing import Any, Optional


def create_search_agent() -> dict:
    """
    Create the search agent configuration.

    Returns a dict with:
        - name: str
        - description: str (used by coordinator to decide when to invoke)
        - tools: list[str] (scoped to search operations only)
        - system_prompt: str (instructions for the search agent)

    The description must be detailed enough for the coordinator to know
    WHEN to use this agent (3-4 sentences per Anthropic's guidance).

    The tools list must include ONLY:
        - web_search
        - academic_search
        - news_search
        - bookmark_result
    """
    raise NotImplementedError("Complete this exercise")


def deduplicate_results(results: list[dict]) -> list[dict]:
    """
    Remove duplicate search results by URL, keeping the first occurrence.

    Each result dict contains:
        - url: str
        - title: str
        - snippet: str
        - source_type: str ("web", "academic", "news")
        - retrieved_at: str (ISO timestamp)

    Returns:
        Deduplicated list preserving original order.
    """
    raise NotImplementedError("Complete this exercise")


def handle_search_error(error_response: dict) -> dict:
    """
    Handle a search tool error response, distinguishing access failures
    from valid empty results.

    Args:
        error_response: dict with:
            - isError: bool (True = tool execution failed)
            - content: str (error message or empty result message)
            - query: str (the original search query)

    Returns:
        dict with:
            - action: str ("retry" | "skip" | "escalate")
            - reason: str (why this action was chosen)
            - original_query: str
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test create_search_agent
agent = create_search_agent()
assert isinstance(agent, dict), "Agent must be a dict"
assert "name" in agent, "Agent must have a name"
assert "description" in agent, "Agent must have a description"
assert "tools" in agent, "Agent must have tools"
assert "system_prompt" in agent, "Agent must have a system_prompt"

# Tools must be scoped -- ONLY search tools
allowed_tools = {"web_search", "academic_search", "news_search", "bookmark_result"}
assert set(agent["tools"]) == allowed_tools, \
    f"Tools must be exactly {allowed_tools}, got {set(agent['tools'])}"

# Description must be substantive (3-4 sentences minimum)
assert len(agent["description"]) > 100, \
    f"Description too short ({len(agent['description'])} chars) -- needs 3-4 sentences"

# Test deduplicate_results
test_results = [
    {"url": "https://example.com/a", "title": "A", "snippet": "...",
     "source_type": "web", "retrieved_at": "2026-03-18T10:00:00Z"},
    {"url": "https://example.com/b", "title": "B", "snippet": "...",
     "source_type": "academic", "retrieved_at": "2026-03-18T10:01:00Z"},
    {"url": "https://example.com/a", "title": "A duplicate", "snippet": "...",
     "source_type": "news", "retrieved_at": "2026-03-18T10:02:00Z"},
    {"url": "https://example.com/c", "title": "C", "snippet": "...",
     "source_type": "web", "retrieved_at": "2026-03-18T10:03:00Z"},
]
deduped = deduplicate_results(test_results)
assert len(deduped) == 3, f"Expected 3 results after dedup, got {len(deduped)}"
assert deduped[0]["title"] == "A", "First occurrence should be kept"
assert deduped[1]["title"] == "B", "Order should be preserved"
assert deduped[2]["title"] == "C", "Order should be preserved"

# Test handle_search_error -- access failure
error_result = handle_search_error({
    "isError": True,
    "content": "Network timeout after 30s",
    "query": "climate change impacts 2025",
})
assert error_result["action"] == "retry", \
    f"Access failure should retry, got '{error_result['action']}'"
assert "climate change" in error_result["original_query"]

# Test handle_search_error -- valid empty results
empty_result = handle_search_error({
    "isError": False,
    "content": "No results found for query",
    "query": "xyznonexistenttopic123",
})
assert empty_result["action"] == "skip", \
    f"Empty results should skip, got '{empty_result['action']}'"

print("All checks passed.")
