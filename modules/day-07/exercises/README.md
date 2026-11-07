# Week 1 Integration Exercise: Customer Support Agent

## System Description

You're building a customer support agent system with four components:

### 1. Tool Definitions (`tools.py`)
Four tools the agent can use:
- **get_customer** — Look up a customer by ID. Returns profile data.
- **process_refund** — Issue a refund for a specific order. Requires customer verification first.
- **escalate_to_human** — Hand off to a human agent with context.
- **check_policy** — Verify if an action is allowed by company policy.

Each tool needs a proper description (3-4 sentences), input schema, and response format.

### 2. Hook Configuration (`hooks.py`)
Two hooks enforcing business rules:
- **PreToolUse hook** on `process_refund` — blocks execution unless `get_customer` has been called and verified
- **Stop hook** — quality gate ensuring the agent has addressed the customer's issue before finishing

### 3. Agentic Loop (`agent_loop.py`)
The canonical loop with:
- Correct `stop_reason` branching (tool_use, end_turn, pause_turn)
- Error recovery for tool failures (using isError patterns from Day 6)
- Safety backstop (max iterations as backup, not primary control)

### 4. Orchestrator (`orchestrator.py`)
Hub-and-spoke coordinator that:
- Analyzes customer requests and routes to appropriate handling
- Delegates to the agent loop with scoped tool sets per task type
- Passes structured context to subagents (not raw conversation history)

## Implementation Order

**Build in this order — each file depends on the previous:**

```
tools.py → hooks.py → agent_loop.py → orchestrator.py
```

1. **tools.py** — Define the tool schemas. Everything else references these.
2. **hooks.py** — Configure hooks that reference tool names from tools.py.
3. **agent_loop.py** — Build the loop that executes tools and respects hooks.
4. **orchestrator.py** — Build the coordinator that delegates to agent_loop.

## Verification

After completing all four files, run the structural checks in each file:

```bash
python3 exercises/tools.py
python3 exercises/hooks.py
python3 exercises/agent_loop.py
python3 exercises/orchestrator.py
```

All should print "All structural checks passed."

## What This Tests

This integration exercise maps to real exam scenarios. The exam presents multi-component systems and asks you to identify:
- Which layer is responsible for a specific behavior
- What breaks when a layer is misconfigured
- How to add a new requirement to an existing system

Building the system yourself gives you the mental model to answer these questions.
