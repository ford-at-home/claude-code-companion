# Exercise: Fork Session Behavior

## Scenario

You're working in a Claude Code session debugging a TypeScript application. You've been going back and forth with Claude for 20 messages, and Claude has read several files and made some tool calls.

You decide to try two different approaches to fix a bug. You use `fork_session` to create a new session (Session B) branching from your current session (Session A).

In Session A (the original), Claude writes a new utility file:
```
src/utils.ts
```

This file contains helper functions for the bug fix approach A is trying.

## Your Analysis

**Question 1:** Can Session B's Claude see and read `src/utils.ts`? Why or why not?

**Question 2:** Does Session B's Claude know that Session A created `src/utils.ts`? Why or why not?

**Question 3:** If Session B's Claude also writes to `src/utils.ts` with different content, what happens in Session A?

<!-- Write your answers below -->


## When You're Done

Key things to check:
- [ ] You correctly identified what fork_session branches (conversation history) vs what it doesn't (filesystem)
- [ ] You distinguished between "can see the file" and "knows who created it"
- [ ] You addressed the conflict scenario in Question 3
