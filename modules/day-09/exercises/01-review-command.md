# Exercise: Review Command

## Scenario

Your team wants a `/review` command that every engineer can use immediately after cloning the repository. The command should:

1. Be available to all team members without any local setup
2. Accept a PR number as an argument
3. Fetch the PR diff and comments
4. Ask Claude to summarize the changes and flag potential issues

The exam question reads:

> **Q4.** A team needs a `/review` command available to all engineers immediately on clone. Where should this command be defined?
>
> **(A)** `~/.claude/commands/review.md` on each team member's machine
>
> **(B)** `.claude/commands/review.md` in the project repository
>
> **(C)** `.claude/skills/review/SKILL.md` with `user-invocable: false`
>
> **(D)** As a shell alias in the team's shared `.bashrc`

## Your Analysis

Select the best answer and explain WHY each option is correct or incorrect. For the correct answer, also explain how `$ARGUMENTS` and `!`backtick preprocessing would be used in the command file.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You selected the correct answer
- [ ] You explained the VCS sharing mechanism
- [ ] You identified why each wrong answer fails the "available on clone" requirement
- [ ] You described how the command file would use `$ARGUMENTS` and `!`backtick syntax
