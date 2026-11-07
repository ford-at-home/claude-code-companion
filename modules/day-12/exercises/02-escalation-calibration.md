# Exercise: Escalation Calibration

## Scenario

The exam question reads:

> **Q3.** A customer service agent is running at 55% first-call resolution (FCR), well below the 80% target. Analysis reveals an inverted calibration problem: the agent escalates easy, routine cases to human agents while attempting to handle complex, edge-case scenarios on its own. The team needs to fix the calibration.
>
> Which approach will most effectively fix the inverted calibration?
>
> **(A)** Add explicit escalation criteria with 3-5 few-shot examples showing which cases to handle vs. escalate
>
> **(B)** Add a confidence score threshold — escalate when confidence is below 70%
>
> **(C)** Add an external classifier that categorizes cases before the agent sees them
>
> **(D)** Use sentiment analysis to detect when the agent is struggling

## Your Analysis

Select the best answer. For each option, explain the specific mechanism by which it would (or would not) fix the **inverted calibration** problem.

<!-- Write your answer below -->


## When You're Done

Key things to check:
- [ ] You selected the correct answer
- [ ] You explained WHY the agent has inverted calibration (it doesn't know WHICH cases are easy)
- [ ] You explained why confidence scores reflect model certainty, not case difficulty
- [ ] You explained why sentiment analysis is unreliable for this specific problem
- [ ] You connected few-shot examples to teaching the decision boundary
