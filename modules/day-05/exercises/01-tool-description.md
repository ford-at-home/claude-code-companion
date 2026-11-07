# Exercise: Tool Description Writing

## Scenario

You have a tool with this description:

```
"Retrieves customer information"
```

This description is causing routing problems. Claude sometimes uses this tool when it should use `get_order_details`, and sometimes fails to use it when it should (using `search_customers` instead).

## Your Task

Rewrite this description as a 3-4 sentence, exam-quality tool description that covers:
1. **What** the tool does (specific behavior)
2. **When** to use it (and when NOT to)
3. **Parameters** (what they accept)
4. **Limitations** (what the tool cannot do)

Assume the tool:
- Takes a `customer_id` (string, UUID format) and returns the customer's profile
- Returns name, email, phone, account status, and subscription tier
- Does NOT return order history (that's `get_order_details`)
- Does NOT search by name or email (that's `search_customers`)
- Requires a known customer_id — cannot discover customers

<!-- Write your improved description below -->


## When You're Done

Key things to check:
- [ ] Your description is 3-4 sentences (not a single line, not a paragraph)
- [ ] It specifies WHAT is returned (profile fields)
- [ ] It specifies WHEN to use it vs alternatives (has customer_id, not searching)
- [ ] It specifies LIMITATIONS (no order history, no search, requires known ID)
