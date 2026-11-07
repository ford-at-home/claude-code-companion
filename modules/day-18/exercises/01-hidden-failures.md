# Exercise: Hidden Failure Detection

## Scenario

You are evaluating an invoice processing pipeline that uses Claude to extract structured data from scanned invoices. The pipeline processes three types of invoices:
- **Typed invoices** (65% of volume) -- standard computer-generated PDFs
- **Handwritten invoices** (20% of volume) -- filled out by hand, then scanned
- **Mixed invoices** (15% of volume) -- printed templates with handwritten annotations

The pipeline's overall accuracy metric: **97% correct extractions**.

Your manager is satisfied with this number and wants to push to production. But you suspect the pipeline is hiding a significant failure rate on handwritten invoices.

## Your Analysis

**Question:** How would you detect if this 97% accuracy is hiding a 40% failure rate on handwritten invoices? Describe at least 5 specific investigative steps.

<!-- Write your analysis below -->


## When You're Done

Key things to check:
- [ ] You identified stratification by input type as the first step
- [ ] You mentioned field-level confidence analysis (not just document-level)
- [ ] You included manual sampling of the handwritten subset
- [ ] You considered hallucination patterns (fabricating plausible values vs. returning null)
- [ ] You addressed the null output problem (does the pipeline correctly abstain when it can't read?)
