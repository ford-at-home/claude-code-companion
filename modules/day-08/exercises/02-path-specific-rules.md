# Exercise: Path-Specific Rules

## Scenario

Your team is setting up Claude Code configuration for a large monorepo. The exam question reads:

> **Q6.** A team wants to enforce testing conventions (use `pytest`, follow arrange-act-assert, include docstrings on test functions) only when Claude is working on test files. Which approach is BEST?
>
> **(A)** Create a `.claude/rules/testing.md` file with YAML frontmatter specifying `paths: **/test_*.py`
>
> **(B)** Add the testing conventions to the root `CLAUDE.md` file
>
> **(C)** Create a skill called `/test-conventions` that contains the rules
>
> **(D)** Place a `CLAUDE.md` file in every test subdirectory

## Your Analysis

Select the best answer and explain WHY each option is correct or incorrect. For the wrong answers, identify the specific limitation that disqualifies them.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You selected the correct answer
- [ ] You explained the conditional activation mechanism (paths frontmatter)
- [ ] You identified the specific problem with each wrong answer (not just "it's wrong")
- [ ] You connected your reasoning to how rules scale across diverse codebases
