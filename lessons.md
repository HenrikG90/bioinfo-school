# lessons.md — your prep log

One file for the whole prep. Keep two kinds of entry in **separate subsections each week** — don't mix them in one paragraph.

| Subsection | What goes here | How much detail |
|------------|----------------|-----------------|
| **From the materials** | Notes while watching or reading; answers to each week's reflection exercises | Usually one sentence per video chunk or paper section; reflection exercises can be a short paragraph each |
| **Surprises** | Moments an LLM or agent surprised you — good or bad — in chat or in the IDE | Concrete: tool/model, what you asked, what came back, optional takeaway |

Commit and push weekly. By week 4 this file is one of the most useful artifacts you bring to Brno. (`reflection.md` in week 4 is separate — one final paragraph for assessment.)

---

## From the materials — what to write

While watching or reading, stop every ~20 minutes (or after each major section) and add a line answering:

- *Video:* **What's the one thing I'd want to test from what I just heard?**
- *Paper:* **What claim would I most want to verify on my own data?**

Each week may also assign a **reflection exercise** (structured thinking using the week's mental model). Put those answers here too — they are not required to be personal chat logs.

---

## Surprises — what to write

Add an entry whenever an LLM or agent catches you off guard. Include enough detail that you (or a classmate) could understand the moment months later.

- **When** — approximate date
- **Tool / model** — e.g. ChatGPT (free), Claude, Antigravity agent, Cursor, …
- **What you asked** — paste or paraphrase the prompt; name any file or data involved
- **What happened** — the surprising part
- **Takeaway** (optional) — one line on what you'd do differently

**Bad (too vague):** *"ChatGPT hallucinated something."*

**Good:**

> **2026-05-26 · ChatGPT (free, no browsing)** — Asked: *"What is the Ensembl ID for human BRCA1?"* Answered confidently with `ENSG00000012048` — correct — then cited a made-up paper (*Smith et al., Nature 2019*) and a DOI that 404s. **Takeaway:** right gene, invented provenance; never trust citations without checking.

> **2026-06-03 · Antigravity agent** — Asked it to filter a BED file to chr21. Code ran, printed 1,842 lines, looked plausible. Checked: 0-based coordinates on a file the header said was 1-based. **Takeaway:** spot-check coordinate conventions before trusting counts.

---

## Your entries

(Add below. Newest at the bottom is fine — stay consistent.)

### Week 1

#### From the materials
**Karpathy — Deep Dive into LLMs**
LLMs predict the next token — they don't retrieve facts. This explains 
hallucinated citations and why they miscount residues: tokenization breaks 
sequences arbitrarily, not biologically. Prompting precision is essential. 
One thing I'd test: maybe how prompt length influences answer precsion in differen fields or sub-fields. 

**GeneGPT**
Tool use fixes hallucinations on database queries — the model stops inventing 
gene IDs when it can look them up.
Claim I'd verify: does this hold on less curated databases than NCBI? I'm not sure how the interaction with a database works - should check.

#### Surprises
**2026-06-06 · Claude** — Asked for an interactive visualization. 
The output quality was unexpectedly high — felt closer to a 
designed UI than a generated artifact.

**2026-05-28 · ChatGPT (free)** — Asked it to count the words in 
a paragraph I had written. It gave a wrong number confidently. 
Takeaway: tokenization means the model is not "counting" the 
way a human would — it's predicting a plausible answer.

### Week 2

#### From the materials
**Karpathy — Software Is Changing (Again)**
The Software 1.0/2.0/3.0 framework clicked. The Iron Man analogy 
is the most useful frame I have for thinking about the autonomy 
slider — right now we are building suits and not robots.
One thing I'd test: where exactly on the autonomy slider 
bioinformatics tasks should sit, given how silently wrong the 
output can be.

**ReAct paper**
The reasoning+acting loop is what I was already seeing in 
Antigravity without knowing it had a name. The agent reads files, 
thinks, acts, reads the result, thinks again. Simple but it 
explains a lot of the behavior.

**Reflection — discussion questions**
1. *Other "looks right but isn't" failures:* small off-by-one 
errors like the trap — the kind the agent introduces silently 
because it interpolates patterns from training data without 
understanding the biological context. The faster and more 
confident the agent, the harder these are to catch.

2. *Three ways to validate output in my subfield:*
   - Read the output row by row where possible
   - Check if the numbers are in a realistic range for the 
     measurement (e.g. KTR values I'd expect from the literature)
   - Test with known formulas or reference values

3. *Scaling validation:* build the most efficient checking 
system possible upfront — automated flags for anything outside 
expected ranges, so I don't have to eyeball thousands of rows.

#### Surprises

**2026-06-07 · Antigravity agent (Gemini Flash)** — Gave the 
trap prompt without any hint about coordinate systems. The agent 
identified the 1-based vs 0-based issue on its own and wrote 
correct code immediately. Lesson: the agent sometimes catches 
the trap, sometimes doesn't — you cannot know in advance, so 
you validate every time regardless.

**2026-06-08 · Antigravity agent** — Most surprising thing 
today was not the code but the workflow: the agent coordinates 
files, switches languages, and shows its reasoning in real time. 
The reasoning trace is almost too fast to read, but knowing it 
is there changes how much I trust the output.

**2026-06-06 · General** — The hardest part of the week was 
not the biology or the prompts — it was the environment itself. 
Git, GitHub, IDE, terminals, commits, push — none of it is 
intuitive when you have never worked as a programmer. The 
concepts make sense; the friction is in the interfaces.

### Week 3

#### From the materials

**Jumper Nobel Lecture**
AlphaFold solved a problem that had been open for 50 years and the key insight was using co-evolution across species
a signal — if two positions are always mutated together across millions of sequences, they're probably in contact 
in the 3D structure. One thing I'd test: how pLDDT changes on 
disordered proteins, which by definition have no stable structure.

**CARBON paper**
A foundation model for DNA sequences. Similar philosophy 
to ESM2 but for genomics. Limitations section was the 
most useful part — the model performs well on benchmarks 
but benchmark performance doesn't guarantee real-world utility.


#### Surprises

**2026-06-11 · ColabFold** — Predicted BDNF structure in 
under 5 minutes in a browser. The visualization was 
unexpectedly good. What surprised me most was how 
accessible something this powerful has become.

**2026-06-11 · General reflection** — You can trust the 
model within its narrow context. But the moment you step 
outside it — asking what the protein does in a cell, 
how it behaves under different conditions, what 
post-translational modifications change — the model has 
nothing to say. The risk is forgetting where the boundary 
is and building conclusions on top of a very narrow foundation.

P.S. Exercise C — attempted, library error, agent couldn't move forward, skipped.


### Week 4

#### From the materials

**The three modes of agent-tool interaction**

Mode 1 (agent writes code) is what I used for the KTR script — 
reusable, but errors can be silent until validated.
Mode 2 (agent runs commands directly) is faster for one-off 
checks but leaves nothing reusable behind.
Mode 3 (structured MCP tools) would matter if I ever needed 
to run KTR calculations routinely on incoming patient data — 
a typed, auditable tool instead of re-running a script by hand.

For now, my work is mostly Mode 1: small, reusable scripts on 
research datasets. Mode 3 becomes relevant only at production 
scale, which isn't where I am yet.
<!-- MCP / BixBench notes -->

#### Surprises

<!-- BioTerm-Bench, MCP demo, failure modes -->
