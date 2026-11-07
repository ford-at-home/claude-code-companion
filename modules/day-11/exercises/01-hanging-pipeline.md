# Exercise: Hanging Pipeline

## Scenario

The exam question reads:

> **Q10.** A team adds Claude Code to their CI pipeline for automated PR security review. The pipeline step is:
>
> ```bash
> claude "Analyze this PR for security issues"
> ```
>
> The pipeline hangs on every run, eventually timing out after 30 minutes. No output is produced. What is the most likely cause, and how should it be fixed?

## Your Analysis

1. Identify the root cause of the hang
2. Write the corrected command
3. Add at least 3 additional flags you would recommend for a production CI pipeline, explaining why each is needed

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You identified the missing `-p` flag as the root cause
- [ ] Your corrected command includes `-p`
- [ ] You recommended `--output-format json` for machine-readable output
- [ ] You recommended `--max-turns` as a safety backstop
- [ ] You explained WHY each additional flag matters in CI
