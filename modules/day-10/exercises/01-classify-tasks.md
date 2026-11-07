# Exercise: Classify Tasks

## Scenario

You're mentoring a junior engineer on when to use Plan Mode vs. direct execution in Claude Code. They've compiled a list of tasks they need to complete this sprint and want your guidance on which mode to use for each.

## Instructions

For each task below, classify it as **Plan Mode** or **Direct Execution**. Provide a one-sentence justification for each.

| # | Task | Mode | Justification |
|---|------|------|---------------|
| 1 | Rename a variable from `usr` to `user` across the codebase | | |
| 2 | Refactor the authentication middleware to support OAuth2 in addition to JWT | | |
| 3 | Fix a typo in the README ("recieve" → "receive") | | |
| 4 | Add structured logging to 5 microservices that currently use `console.log` | | |
| 5 | Change one API endpoint's return type from `string` to `{ value: string, metadata: object }` | | |
| 6 | Migrate the database schema from single-tenant to multi-tenant | | |
| 7 | Update the `lodash` dependency from v4.17.20 to v4.17.21 | | |
| 8 | Redesign error handling across 3 modules to use a centralized error class hierarchy | | |

## Your Analysis

<!-- Fill in the table above, then write a brief summary of your decision criteria below -->


## When You're Done

Key things to check:
- [ ] You correctly identified the 3+ file threshold for Plan Mode
- [ ] You classified single-file, well-defined tasks as Direct Execution
- [ ] Your justifications reference file count, complexity, or cross-cutting concerns
- [ ] You didn't default everything to Plan Mode "just to be safe"
