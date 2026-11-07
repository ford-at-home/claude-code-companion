"""
Exercise: Canonical Agentic Loop
Day: 01 | Domain: D1
API Required: No

You are building the core agentic loop that drives all Claude-based agents.
The loop must be governed entirely by `stop_reason` -- no text parsing,
no arbitrary iteration caps as primary exit conditions.

Instructions:
1. Implement `run_agentic_loop` that calls the Messages API in a loop
2. Handle `tool_use`: execute the tool, append assistant message, append tool_result
3. Handle `end_turn`: return Claude's final text response
4. Handle `pause_turn`: re-send messages without adding new user content
5. Include a safety backstop (max iterations) that logs a warning but does NOT
   replace stop_reason as the primary control signal

Hints:
- The assistant message (with tool_use block) must be appended BEFORE the tool_result
- tool_result goes in a user message with the matching tool_use_id
- Do NOT add any text content after the tool_result -- this is anti-pattern #2
"""

from typing import Any


# Simulated tool registry -- maps tool names to callables
TOOL_REGISTRY: dict[str, callable] = {
    "get_weather": lambda **kwargs: f"72°F and sunny in {kwargs.get('location', 'unknown')}",
    "get_time": lambda **kwargs: "2026-03-18T14:30:00Z",
}

MAX_ITERATIONS = 50  # Safety backstop only


def execute_tool(tool_name: str, tool_input: dict[str, Any]) -> str:
    """Execute a tool by name with the given input. Returns the tool's output as a string."""
    raise NotImplementedError("Complete this exercise")


def run_agentic_loop(client: Any, messages: list[dict], tools: list[dict]) -> str:
    """
    Run the canonical agentic loop.

    Args:
        client: An object with a messages.create() method (Anthropic client)
        messages: Initial conversation messages
        tools: Tool definitions for the API call

    Returns:
        Claude's final text response when stop_reason == "end_turn"
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

def _mock_response(stop_reason, content):
    """Helper to create mock API responses for testing."""
    class MockResponse:
        def __init__(self, sr, c):
            self.stop_reason = sr
            self.content = c
    return MockResponse(stop_reason, content)


class _MockTextBlock:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class _MockToolUseBlock:
    def __init__(self, tool_id, name, tool_input):
        self.type = "tool_use"
        self.id = tool_id
        self.name = name
        self.input = tool_input


# Verify execute_tool works with registry
assert execute_tool("get_weather", {"location": "Seattle"}) == "72°F and sunny in Seattle"
assert execute_tool("get_time", {}) == "2026-03-18T14:30:00Z"

# Verify execute_tool handles unknown tools gracefully
try:
    execute_tool("nonexistent_tool", {})
    assert False, "Should have raised an error for unknown tool"
except (KeyError, ValueError):
    pass  # Expected

# Verify run_agentic_loop signature exists and is callable
import inspect
sig = inspect.signature(run_agentic_loop)
params = list(sig.parameters.keys())
assert params == ["client", "messages", "tools"], f"Expected params [client, messages, tools], got {params}"

print("All structural checks passed.")
