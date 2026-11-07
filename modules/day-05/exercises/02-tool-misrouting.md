# Exercise: Tool Misrouting Diagnosis

## Scenario

A support agent has access to 8 tools. In testing, Claude routes to the wrong tool 28% of the time — particularly confusing `update_customer_email` with `update_customer_profile` and `search_orders` with `search_customers`.

The team proposes two fixes:

**(A) Add few-shot examples** to the system prompt showing correct tool selection for 10 common scenarios.

**(B) Rewrite tool descriptions** to be more specific about what each tool does, when to use it, and how it differs from similar tools.

## Your Analysis

**Question:** Why is (B) the correct FIRST step, and why does (A) fail as a first-line fix even though few-shot examples are powerful? Be specific about the mechanism.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You explained that descriptions ARE the selection mechanism (injected into system prompt)
- [ ] You explained why fixing descriptions addresses the root cause
- [ ] You explained why few-shot examples are secondary optimization, not primary fix
- [ ] You mentioned input_examples and the 72% to 90% accuracy stat (if applicable)
