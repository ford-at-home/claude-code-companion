# Exercise: Narrow Decomposition Diagnosis

## Scenario

A research team builds a multi-agent system to produce comprehensive reports on broad topics. The coordinator agent decomposes tasks and delegates to specialized subagents (search, analysis, synthesis, document writing).

A user requests: **"Write a comprehensive report on AI in creative industries."**

The coordinator decomposes this into three research subtasks:
- Digital art and AI-generated imagery
- Graphic design automation
- AI in photography and photo editing

The final report is well-written and well-sourced, but a reviewer notes it **only covers visual arts**. Music composition, creative writing, film production, and game design are entirely absent.

The team considers these fixes:
- (A) Improve the synthesis agent's prompt to identify gaps
- (B) Add a search agent that specifically looks for missing domains
- (C) Add a document review agent that checks for completeness
- (D) Fix the coordinator's task decomposition

## Your Analysis

**Question:** Why is option (D) the root cause fix, and why are options A, B, and C treating symptoms rather than the disease? Be specific about the mechanism.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You identified task decomposition as the root cause, not agent capability
- [ ] You explained WHY synthesis/search/doc agents can't fix a decomposition problem
- [ ] You provided a better decomposition (at least 4-5 broader categories)
- [ ] You connected this to the hub-and-spoke model's information flow
