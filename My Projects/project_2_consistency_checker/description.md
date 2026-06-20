# Project 2 — Manuscript Consistency Checker

## What it does
An agent that reads a manuscript (.docx) and a results file (.csv), then checks that every number cited in the text (AUC, p-values, N, beta coefficients) exactly matches the values in the data file. Discrepancies are flagged with location and suggested correction.

## My use case
My manuscript reports AUC, ROC values, and group sizes from a machine learning analysis of kynurenine metabolites. This agent catches copy-paste errors before submission.

## How to swap this for your research
Provide your own .docx manuscript and .csv results file. The agent reads both and cross-checks automatically — no domain knowledge required from your partner.

## Agent architecture
1. **Parse manuscript** — extract all numeric values and their context
2. **Parse results file** — index all metrics by name/label
3. **Compare** — flag mismatches with exact location in text

## Expected output
- List of matched values (confirmed correct)
- List of flagged discrepancies with line reference and correct value
