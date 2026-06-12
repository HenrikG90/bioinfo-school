# Week 3 Results

Use this file for the short Week 3 write-up. Keep it factual: what ran, what failed, what you checked, and what you would trust.

## Exercise A: Structure Prediction

- Tool or notebook: ColabFold v1.6.1 (AlphaFold2)
- Sequence or target: BDNF mature form (119 aa)
- Mean pLDDT: high overall, visually estimated ~80-90 for core
- Low-confidence regions: termini and some peripheral loops (pale/white)
- PAE observation: not inspected in detail
- Would you trust this prediction for a biological claim? 
  Yes for the high-confidence core. No for the low-confidence 
  regions — those would need experimental validation.

## Exercise B: Protein Embeddings

- Model: ESM2 (via HuggingFace)
- Number of sequences: 45
- Pooling choice: CLS token (per-sequence embedding)
- Plot files: UMAP scatter plot by protein family
- Did known families cluster? Yes — GPCR and immunoglobulin 
  showed tight clusters, kinases more spread out
- One validation check: visual inspection of UMAP clustering 
  by family label

## Exercise C: Optional Genomic Benchmarks

- Attempted but hit ImportError on genomic_benchmarks library. 
  Could not resolve quickly. Optional exercise — skipped.

## Surprises

- My biology itself feels weak while doing these tasks
- Hard to interpret: UMAP axes have no biological meaning — 
  just compressed coordinates. Took time to accept that.
- Validation habit to reuse: always check model confidence 
  scores before trusting any output. Don't step outside the 
  model's narrow context without experimental grounding.
