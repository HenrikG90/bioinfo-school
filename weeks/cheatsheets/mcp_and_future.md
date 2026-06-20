# MCP and where this is going (~1h)

Forward-looking, but grounded.

## MCP Demo: NCBI & PubMed Search
Let's see the Model Context Protocol (MCP) in action. Instead of having the agent write a custom API wrapper or parse raw CLI/curl output (Mode 1 and Mode 2), we connect directly to an NCBI/PubMed MCP server.

Through this structured interface, the agent can query PubMed:
- **Task:** Find recent reviews on the role of the evolutionary conservation model "Evo2" in genomic design or general genomic language models published in 2025/2026.
- **How it works:** The agent sends a structured request to the MCP tool (`pubmed_search`), which returns a clean JSON structure containing titles, PMIDs, and abstracts. The agent interprets these directly without fragile regex parsing.

Here is a typical interaction via MCP:
```json
// Agent tool call to PubMed MCP
{
  "name": "ncbi_pubmed_search",
  "arguments": {
    "query": "genomic language models review 2025",
    "retmax": 3
  }
}
```
The output is returned as structured data, avoiding the "HTML scraping" or "txt parsing" headaches of raw CLI commands.

---

## Three Threads (A Brief & Skeptical Outlook)

### 1. The MCP Ecosystem in Bio: What's Here and What's Missing
* **What exists today:** Standard wrappers for big APIs (NCBI E-utilities, ChEMBL, PubChem, and BioMCP for Genotype-Ontology mappings).
* **What's missing:** Most niche bioinformatic command-line tools. There is no `samtools` MCP server, no `bedtools` MCP server, and no `bwa` MCP server. If you want them to be accessible as clean tools, you have to build the wrappers yourself.
* **Why this matters:** Agent capability does not scale solely with model size or reasoning parameters. It scales with the richness and robustness of the tool ecosystem. If the agent has to fall back to Mode 2 (running shell commands and guessing flags) for every niche tool, reliability drops precipitously.

### 2. Agentic Pipelines and "AI Scientist" Systems
* **The State of the Art:** Frameworks like BixBench, Aviary, and Sakana AI's "AI Scientist" attempt to automate complete end-to-end scientific workflows.
* **The Reality Check:** On real, complex bioinformatics tasks (e.g., BixBench), state-of-the-art frontier agents hover around **~17% accuracy**.
* **The Practical Takeaway:** These systems are currently best viewed as useful, highly calibrated assistants for specific sub-tasks rather than autonomous, general-purpose bioinformaticians. Treat them as junior compilers for workflows, not independent researchers.

### 3. The Bio Foundation Model Frontier
* **Where we are heading:** Models are scaling from simple sequence representations to multimodal structures (ESM3, AlphaFold3, Evo2, and single-cell foundations like scFoundation). They are beginning to generate sequence, structure, and function coordinates jointly.
* **What remains unsolved:** 
  * **Dynamics & Ensembles:** Most structural models predict static, crystallized snapshots rather than thermodynamic ensembles and conformational dynamics.
  * **Post-Translational & Environmental States:** Glycosylation, phosphorylation, pH, and ligand concentrations are often ignored or poorly modeled.
  * **The Horizon:** The Bio FM cheat sheet you read in Week 3 will likely be outdated in 6 months. Keep your validation pipelines flexible.

---

## On-ramp to Brno: Day One Onsite (Mon 22.6)

When you show up in Brno on Monday morning, bring:
1. **Your genomic-benchmarks repository** (fully reproducible with your new `pyproject.toml` and `uv` setup).
2. **Your updated [lessons.md](../lessons.md)**.
3. **A list of three specific tools or pipelines you want to build** (e.g., a custom MCP server for a tool you use daily, an agentic evaluation script, or a fine-tuning pipeline).

We will kick off by exchanging repositories and attempting to run each other's code. If your `pyproject.toml` is correct, this will take two minutes. If not, it will be our first debugging session!
