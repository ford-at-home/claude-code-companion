"""
Exercise: Interview Pattern Prompt
Day: 10 | Domain: D3
API Required: No

The interview pattern is a requirements-gathering technique where Claude asks
clarifying questions BEFORE implementing. This prevents the common failure mode
of Claude charging ahead with assumptions that don't match your intent.

Instructions:
1. Implement `build_interview_prompt` that takes a task description
2. Return a prompt string that instructs Claude to:
   - NOT implement anything yet
   - Ask exactly 5 clarifying questions before proceeding
   - Cover: constraints, edge cases, priorities, testing requirements, and
     integration points
   - Only implement AFTER receiving answers to all questions
3. The prompt should work for ANY task description (not hardcoded to one scenario)

Hints:
- The prompt is the return value -- you're building a string, not calling an API
- Think about what makes a good clarifying question (specific, actionable, reveals hidden assumptions)
- The interview pattern works because Claude doesn't know what it doesn't know,
  but it CAN identify gaps when prompted to ask
"""


def build_interview_prompt(task_description: str) -> str:
    """
    Build a prompt that instructs Claude to ask 5 clarifying questions
    before implementing the given task.

    Args:
        task_description: A brief description of the task to implement

    Returns:
        A prompt string with interview instructions and the task context
    """
    raise NotImplementedError("Complete this exercise")


# --- Do not modify below this line ---

# Verify function exists and returns a string
result = build_interview_prompt("Add a caching layer to the API")
assert isinstance(result, str), f"Expected str, got {type(result)}"
assert len(result) > 100, "Prompt seems too short to contain meaningful interview instructions"

# Verify the task description is included in the output
assert "caching" in result.lower(), "The task description should appear in the prompt"

# Verify key interview elements are present
result_lower = result.lower()
assert any(word in result_lower for word in ["question", "ask", "clarif"]), \
    "Prompt should instruct Claude to ask questions"
assert any(word in result_lower for word in ["before", "first", "prior", "until"]), \
    "Prompt should indicate questions come BEFORE implementation"
assert any(word in result_lower for word in ["implement", "execut", "build", "code", "writ"]), \
    "Prompt should reference implementation happening after questions"

# Verify it works with a different task (not hardcoded)
result2 = build_interview_prompt("Migrate the database to PostgreSQL")
assert "postgresql" in result2.lower() or "postgres" in result2.lower() or "database" in result2.lower(), \
    "Prompt should include the specific task description, not be hardcoded"

print("All structural checks passed.")
