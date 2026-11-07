"""
Exercise: Scoped Tool Set Design
Day: 05 | Domain: D2
API Required: No

Design tool sets for a 3-agent research system. Each agent has a
specific role and should get ONLY the tools it needs (4-5 max per agent).

The three agents:
1. Search Agent — finds information from web and academic sources
2. Analysis Agent — reads documents and extracts structured findings
3. Synthesis Agent — combines findings into a final report

Instructions:
1. Implement `build_agent_tool_sets` returning a dict of agent_name -> tool list
2. Each tool must have: name, description (3-4 sentences), and input_schema
3. Each agent gets at most 5 tools
4. Tools should NOT overlap between agents — clear role boundaries
5. Descriptions must be specific enough to prevent misrouting

Hints:
- Think about what each agent ACTUALLY needs to do, not what might be useful
- The search agent finds things. The analysis agent reads and extracts.
  The synthesis agent combines and writes. Keep them separate.
- Tool descriptions should mention what the tool does NOT do to prevent confusion
"""

from typing import Any


def build_agent_tool_sets() -> dict[str, list[dict]]:
    """
    Design scoped tool sets for a 3-agent research system.

    Returns:
        Dict mapping agent names to their tool definitions.
        Each tool definition has:
        - "name": str
        - "description": str (3-4 sentences)
        - "input_schema": dict (JSON schema for parameters)

    Constraints:
        - Each agent gets at most 5 tools
        - No tool appears in multiple agents' sets
        - Descriptions must be specific and non-overlapping
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

tool_sets = build_agent_tool_sets()

# Must have exactly 3 agents
assert set(tool_sets.keys()) == {"search", "analysis", "synthesis"}, \
    f"Expected agents: search, analysis, synthesis. Got: {set(tool_sets.keys())}"

# Each agent gets at most 5 tools
for agent, tools in tool_sets.items():
    assert len(tools) <= 5, f"{agent} has {len(tools)} tools (max 5)"
    assert len(tools) >= 2, f"{agent} has {len(tools)} tools (need at least 2)"

# Each tool has required fields
for agent, tools in tool_sets.items():
    for tool in tools:
        assert "name" in tool, f"Tool in {agent} missing 'name'"
        assert "description" in tool, f"Tool {tool.get('name', '?')} missing 'description'"
        assert "input_schema" in tool, f"Tool {tool.get('name', '?')} missing 'input_schema'"
        # Description should be substantive (3+ sentences ~ 100+ chars)
        assert len(tool["description"]) >= 80, \
            f"Tool {tool['name']} description too short ({len(tool['description'])} chars). Need 3-4 sentences."

# No tool name appears in multiple agents
all_names = []
for tools in tool_sets.values():
    all_names.extend(t["name"] for t in tools)
assert len(all_names) == len(set(all_names)), \
    f"Duplicate tool names found: {[n for n in all_names if all_names.count(n) > 1]}"

print("All structural checks passed.")
print(f"  search: {len(tool_sets['search'])} tools")
print(f"  analysis: {len(tool_sets['analysis'])} tools")
print(f"  synthesis: {len(tool_sets['synthesis'])} tools")
print(f"  total unique tools: {len(all_names)}")
