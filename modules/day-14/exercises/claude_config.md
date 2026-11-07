# Exercise: Claude Configuration Hierarchy

## Instructions

Design the complete CLAUDE.md configuration hierarchy for the claims-platform monorepo described in the scenario README. You need to provide:

### 1. Directory Tree

Show the full file tree of all `.claude/` configuration files, including:
- Root `.claude/CLAUDE.md`
- All `.claude/rules/` files with their glob patterns
- Any domain-specific CLAUDE.md files

### 2. File Contents

Write the actual content for each file. Keep each file under 200 lines. For each file, explain:
- **What it contains** and why
- **When it loads** (always, lazy, or conditional via glob)
- **What it intentionally does NOT contain** and why that content belongs elsewhere

### 3. Design Decisions

Answer these questions:
- Why use `.claude/rules/` with glob patterns instead of putting everything in root CLAUDE.md?
- Should frontend conventions go in `.claude/rules/frontend.md` or `frontend/CLAUDE.md`? What's the tradeoff?
- How would you handle a new team member who needs to understand the configuration structure?

## Your Design

<!-- Write your configuration hierarchy below -->


## When You're Done

Key things to check:
- [ ] Root CLAUDE.md contains only team-wide conventions (not domain-specific)
- [ ] Domain rules use `paths` frontmatter for conditional activation
- [ ] Test conventions have their own rule file with test-file glob patterns
- [ ] No single file exceeds 200 lines
- [ ] You explained the lazy-loading / conditional activation rationale
