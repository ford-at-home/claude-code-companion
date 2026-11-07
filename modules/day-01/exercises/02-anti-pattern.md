# Exercise: Anti-Pattern Diagnosis

## Scenario

A team has deployed a customer service agent that handles order lookups and refunds. The agent's workflow is:

1. `get_customer` — look up customer by email
2. `get_orders` — retrieve the customer's recent orders
3. `process_refund` — issue a refund for a qualifying order

In production monitoring, the team discovers that the agent **skips the `get_customer` step 12% of the time**, jumping directly to `get_orders` with a hardcoded customer ID or hallucinated value. The agent otherwise completes successfully when it does call `get_customer`.

The team's agentic loop includes this code:

```python
for i in range(10):
    response = client.messages.create(...)
    if response.stop_reason == "tool_use":
        # execute tool, append result
        pass
    elif response.stop_reason == "end_turn":
        return response.content[0].text
    # If we've done 10 iterations, break anyway
return "Max iterations reached"
```

## Your Analysis

**Question:** Which of the three documented anti-patterns is most likely causing the `get_customer` skip? Explain the mechanism -- HOW does this anti-pattern cause the specific failure described?

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You identified the correct anti-pattern (there's one primary culprit)
- [ ] You explained the MECHANISM, not just named the pattern
- [ ] You connected the anti-pattern to the specific symptom (12% skip rate)
- [ ] You noted why the other two anti-patterns are less likely causes
