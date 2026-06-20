# Project 1 — Literature Monitoring Agent

## What it does
An agent that automatically searches PubMed for recent papers on a given research topic, filters them by relevance, and drafts a short "gap in the literature" paragraph ready to paste into a manuscript.

## My use case
Query: `kynurenine pathway bipolar disorder temperament`
Output: summary of recent findings + a draft paragraph positioning my KynTemps study relative to existing work.

## How to swap this for your research
Change the query string to your own topic (e.g. `serotonin schizophrenia cognitive function`). The agent logic stays identical.

## Agent architecture
1. **Fetch** — query PubMed API with predefined search terms
2. **Filter + score** — LLM evaluates relevance of each abstract
3. **Draft** — LLM writes a 3–5 sentence "state of the art" paragraph

## Expected output
- Ranked list of relevant papers (title, year, key finding)
- Draft paragraph for manuscript introduction
