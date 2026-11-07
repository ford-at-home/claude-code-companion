# Exercise: Batch vs. Sync

## Scenario

The exam question reads:

> **Q11.** Your manager proposes using the Message Batches API for two use cases to save costs:
>
> 1. **Overnight report generation** — Every night, generate summary reports for 500 insurance claims processed that day. Each report takes one claim's data as input and produces a structured summary. No tool calling needed.
>
> 2. **Pre-merge PR checks** — For every pull request, run an automated code review that reads the diff, checks related test files, searches for similar patterns in the codebase, and produces a findings report.
>
> Evaluate both use cases. For each, state whether the Batch API is appropriate and explain why.

## Your Analysis

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You correctly identified overnight reports as a GOOD batch candidate
- [ ] You correctly identified pre-merge checks as a BAD batch candidate
- [ ] You explained latency/interactivity (async 24h window, live client-side tool round-trips) as the blocker for PR checks — not a "batches can't do multi-turn/tools" myth
- [ ] You mentioned the 50% cost savings for the batch use case
- [ ] You noted that latency matters for PR flow (developers waiting on merge)
