# Exercise: Error Propagation Analysis

## Scenario

A multi-agent research system has a search subagent that calls a web search tool. During a research task on "renewable energy adoption rates," the web search tool times out after 30 seconds.

The team is debating four approaches to handling this error:

**(A) Return a structured error with context:**
```json
{
  "isError": true,
  "content": [{"type": "text", "text": "Web search timed out after 30s for query 'renewable energy adoption rates'. This is likely a transient network issue. The query is valid and may succeed on retry. Alternative: try a more specific query like 'solar energy adoption rates 2025' to reduce result set size."}]
}
```

**(B) Return a generic error status:**
```json
{
  "isError": true,
  "content": [{"type": "text", "text": "Error: search failed"}]
}
```

**(C) Suppress the error silently:**
```json
{
  "isError": false,
  "content": [{"type": "text", "text": "No results found."}]
}
```

**(D) Terminate the entire workflow:**
Raise an exception that propagates to the coordinator, which restarts the research from scratch.

## Your Analysis

**Question:** Why is (A) the best approach? For each of the other options (B, C, D), explain the specific failure mode it creates.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You explained why structured context enables intelligent recovery
- [ ] You identified B's failure mode (loss of diagnostic information)
- [ ] You identified C's failure mode (conflating access failure with empty result)
- [ ] You identified D's failure mode (unnecessary restart vs resume-from-failure)
- [ ] You connected to the principle "resume from failure, don't restart"
