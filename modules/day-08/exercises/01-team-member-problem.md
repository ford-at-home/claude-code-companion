# Exercise: Team Member Problem

## Scenario

Your team has been using Claude Code for three months. All five existing team members have a consistent experience: Claude always runs `pytest` with the `--strict-markers` flag, uses the team's custom fixture library, and follows the "arrange-act-assert" pattern in test code.

A new team member, Priya, clones the repository and starts using Claude Code. She reports that Claude doesn't follow any of the testing conventions. It writes tests without the custom fixtures, doesn't use `--strict-markers`, and structures tests differently. The existing team members are baffled — "it works fine for us."

**Question:** What is the most likely cause of this problem, and how should the team fix it so every engineer — current and future — gets the testing conventions automatically on clone?

## Your Analysis

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You identified which level of the hierarchy the conventions are currently stored at
- [ ] You explained WHY existing members see the conventions but Priya does not
- [ ] You proposed a fix that works for ALL future team members on clone
- [ ] You chose the right target location (project-level or rules)
