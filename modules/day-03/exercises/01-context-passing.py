"""
Exercise: Structured Context Passing
Day: 03 | Domain: D1
API Required: No

A synthesis subagent needs to combine findings from web search results and
document analysis into a coherent summary with proper source attribution.
The subagent starts with an empty context -- everything it needs must be
in the prompt string you build.

Instructions:
1. Implement `build_synthesis_prompt` that creates a structured prompt
2. Include metadata (source URLs, document names, page numbers) SEPARATED
   from content
3. Use numbered claim-source mappings so every claim is traceable
4. Define the subagent's scope: what to synthesize, what format to produce,
   what to exclude

Hints:
- Think about what a human researcher needs to write a synthesis: the claims,
  where they came from, and what quality standards to meet
- Numbered references make claims verifiable: "Claim 3 [Source 2]" vs
  "research shows..."
- Metadata and content serve different purposes -- don't mix them
"""

from typing import Any


def build_synthesis_prompt(
    web_results: list[dict],
    doc_analysis: list[dict],
) -> str:
    """
    Build a structured prompt for a synthesis subagent.

    Args:
        web_results: List of web search findings, each with:
            - "url": str (source URL)
            - "title": str (page title)
            - "retrieved_at": str (ISO timestamp)
            - "claims": list[str] (extracted claims from this source)

        doc_analysis: List of document analysis findings, each with:
            - "doc_name": str (document filename)
            - "doc_type": str (e.g., "pdf", "report", "whitepaper")
            - "page_numbers": list[int] (relevant pages)
            - "claims": list[str] (extracted claims from this document)

    Returns:
        A structured prompt string for the synthesis subagent
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Test data
sample_web = [
    {
        "url": "https://example.com/ai-trends-2026",
        "title": "AI Trends in Enterprise Software",
        "retrieved_at": "2026-03-15T10:30:00Z",
        "claims": [
            "Enterprise AI adoption grew 40% year-over-year in 2025",
            "Tool-use agents are the fastest-growing category",
        ],
    },
    {
        "url": "https://research.example.org/agent-survey",
        "title": "Agent Architecture Survey 2026",
        "retrieved_at": "2026-03-15T10:32:00Z",
        "claims": [
            "Hub-and-spoke is the dominant multi-agent pattern",
            "Context isolation reduces error propagation by 60%",
        ],
    },
]

sample_docs = [
    {
        "doc_name": "anthropic-agent-patterns.pdf",
        "doc_type": "whitepaper",
        "page_numbers": [4, 7, 12],
        "claims": [
            "Subagent tool sets should be scoped to the role (~4-5 rule of thumb)",
            "Coordinator prompts should specify goals, not procedures",
        ],
    },
]

prompt = build_synthesis_prompt(sample_web, sample_docs)

# Structural checks
assert isinstance(prompt, str), "Must return a string"
assert len(prompt) > 200, "Prompt is too short -- needs structured content"

# Must include source metadata
assert "example.com/ai-trends-2026" in prompt, "Must include source URLs"
assert "anthropic-agent-patterns.pdf" in prompt, "Must include document names"

# Must include claims
assert "40%" in prompt, "Must include claim content"
assert "hub-and-spoke" in prompt.lower(), "Must include claim content"

# Must have some numbering or referencing structure
import re
has_numbering = bool(re.search(r'(\d+[\.\):]|\[.*\d+.*\]|source\s*\d+|claim\s*\d+)', prompt.lower()))
assert has_numbering, "Must use numbered references for traceability"

print("All structural checks passed.")
