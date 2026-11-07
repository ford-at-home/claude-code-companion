# Exercise: Fork Skill

## Scenario

You need to create a skill that analyzes a codebase's architecture — identifying patterns, dependencies between modules, and potential architectural concerns. This skill should:

1. Run in an isolated subagent so it doesn't pollute the main conversation context
2. Be read-only (no file modifications)
3. Accept a directory path as an argument
4. Use Glob, Grep, and Read to explore the codebase
5. Return a structured summary of findings

## Instructions

Write a complete `SKILL.md` file for this skill. Include:

1. **YAML frontmatter** with all relevant fields (`context`, `agent`, `allowed-tools`, `argument-hint`, `name`, `description`)
2. **Preprocessing commands** using `!`backtick syntax to gather initial context (e.g., directory listing, file count)
3. **A prompt body** that instructs Claude to analyze the codebase systematically

Your SKILL.md should be a working file that could be placed in `.claude/skills/architecture-review/SKILL.md`.

<!-- Write your SKILL.md content below -->

```markdown
# Replace this with your SKILL.md content
```

## When You're Done

Key things to check:
- [ ] You included `context: fork` in frontmatter (isolation requirement)
- [ ] You specified `agent: Explore` or equivalent read-only agent
- [ ] You listed appropriate `allowed-tools` (read-only tools only)
- [ ] You used `$ARGUMENTS` for the directory path
- [ ] You included `!`backtick preprocessing for initial context gathering
- [ ] Your prompt body gives Claude a systematic analysis approach
