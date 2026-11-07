# Exercise: Stop Hook vs Prompt-Based Quality Check

## Scenario

Your team is building a code review agent. Before the agent finishes, you want to ensure it has:
1. Checked for security vulnerabilities
2. Verified test coverage exists for changed files
3. Flagged any TODO comments that need resolution

You're deciding between two approaches:

**Approach A — Prompt instruction:**
Add to the system prompt: "Before finishing your review, verify that you have checked for security vulnerabilities, verified test coverage, and flagged TODO comments. Do not end your turn until all three checks are complete."

**Approach B — Stop hook:**
Configure a Stop hook (type: `prompt`) that evaluates whether the agent's output includes all three categories of findings. If any category is missing, the hook returns `"decision": "block"` to force the agent to continue.

## Your Analysis

**Question:** When should you use a Stop hook (Approach B) vs a prompt-based quality check (Approach A)? What are the specific failure modes of each approach? Is there a scenario where Approach A is actually preferable?

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You identified the deterministic vs probabilistic distinction
- [ ] You described specific failure modes for the prompt approach (context pressure, conversation length)
- [ ] You identified when prompt-based guidance IS preferable (advisory quality, subjective judgment)
- [ ] You connected hooks to "must-have" and prompts to "nice-to-have"
