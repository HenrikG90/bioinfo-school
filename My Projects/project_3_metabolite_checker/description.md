# Project 3 — Metabolite Range Agent

## What it does
An agent that autonomously searches databases (PubMed, HMDB) for physiologically expected plasma levels of kynurenine pathway metabolites, then compares them against values in a dataset and flags anomalous values with bibliographic context.

## My use case
My dataset (BIPLONG, ~202 participants) contains plasma levels of KYN metabolites. This agent checks whether any values fall outside ranges reported in comparable studies, helping distinguish biological outliers from measurement errors.

## How to swap this for your research
Replace the metabolite list with your own biomarkers. The search + compare logic is identical.

## Agent architecture
1. **Search** — query PubMed/HMDB for reference ranges for each metabolite
2. **Extract ranges** — LLM pulls min/max/mean values from retrieved sources
3. **Compare** — flag dataset values outside the reference range
4. **Contextualize** — attach the source citation to each flagged value

## Expected output
- Reference range table (metabolite | expected range | source)
- Flagged outliers from dataset with bibliographic context
