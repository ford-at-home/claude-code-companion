# Exercise: Resume vs. Fresh Start

## Scenario

You are a solutions architect advising a team on Claude Code session management. For each of the following situations, decide: **resume the existing session** or **start a fresh context window**? Explain your reasoning.

## Situations

### 1. Mid-Refactoring, Hit Context Limit
You're halfway through a large refactoring across 8 files. Claude has been working for a while and auto-compaction just fired. Three files are done, five remain.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


### 2. Debugging, 3 Failed Fix Attempts
You've been debugging a failing test for 20 minutes. Claude has suggested three different fixes, and all three were wrong. The conversation is getting circular.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


### 3. Code Review, Continue from Yesterday
Yesterday you started reviewing a PR with Claude. You got through 4 of 7 files. Today you want to finish the remaining 3 files.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


### 4. Starting a New Feature in Same Repo
You just finished a bug fix in the payments module. Now you want to start implementing a new search feature in the same repo.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


### 5. CI Pipeline Keeps Failing, 30 Minutes In
You've been debugging a CI pipeline failure for 30 minutes with Claude. The conversation has been productive -- you've narrowed it down to a permissions issue but haven't found the fix yet.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


### 6. Complex Multi-File Change, Halfway Done
You're implementing a feature that touches 12 files. Six are done and committed. You're approaching the context limit but haven't hit it yet.

**Decision:** <!-- resume / fresh -->

**Reasoning:**
<!-- Write your reasoning below -->


## When You're Done

Key things to check:
- [ ] You applied the "2 failed corrections then /clear" rule correctly
- [ ] You distinguished between active debugging (resume) and polluted context (fresh)
- [ ] You considered external state (git commits, scratchpad files) for reconstruction
- [ ] You identified when `/compact` with focus directives is the right middle ground
