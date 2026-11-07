# Cross-Domain Integration: Multi-Agent Research Pipeline

## What You're Building

A research pipeline that takes a topic, searches for sources, analyzes them, and produces a synthesis report with citations. The pipeline has five components:

```
coordinator.py
├── search_agent.py      (finds sources)
├── analysis_agent.py    (extracts claims, scores confidence)
├── synthesis_agent.py   (produces report with citations)
└── hooks.py             (quality enforcement)
```

## Implementation Order

Build in this order. Each component builds on the previous:

1. **search_agent.py** -- Agent definition with scoped tools for finding sources. Handles search errors, deduplicates results, preserves source metadata.

2. **analysis_agent.py** -- Agent definition with scoped tools for analyzing documents. Extracts claims with numbered references, scores confidence per claim, detects conflicting sources.

3. **synthesis_agent.py** -- Agent definition with scoped tools for producing the final report. Uses the case facts pattern to preserve numerical data during progressive synthesis. Formats citations.

4. **hooks.py** -- Quality enforcement gates. PreToolUse hook blocks synthesis before analysis completes. Stop hook verifies report meets quality criteria.

5. **coordinator.py** -- Hub-and-spoke orchestrator. Decomposes the topic broadly, dispatches agents in parallel where possible, passes structured context between phases, handles errors with resume-not-restart.

## Domain Map

Each component exercises specific certification domains:

| Component | Primary Domain | Key Concepts |
|-----------|---------------|--------------|
| search_agent | D2 (Tools) | Scoped tool sets, isError distinction, tool descriptions |
| analysis_agent | D4 (Prompting) | Explicit criteria, structured output, confidence scoring |
| synthesis_agent | D5 (Context) | Case facts pattern, progressive synthesis, citations |
| hooks | D1 (Architecture) | Deterministic enforcement, PreToolUse/Stop hooks |
| coordinator | D1 (Architecture) | Hub-and-spoke, parallel execution, error propagation |

## Running the Exercises

Each file is self-contained with self-check assertions at the bottom. Implement the functions, then run the file:

```bash
python exercises/search_agent.py
python exercises/analysis_agent.py
python exercises/synthesis_agent.py
python exercises/hooks.py
python exercises/coordinator.py
```

Each file prints `All structural checks passed.` when its structure is correct. When all five pass, you've completed the Week 3 integration.
