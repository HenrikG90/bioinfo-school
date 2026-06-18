# Agent Rules & Conventions

- **Explain simply**: Always explain biological and technical concepts 
  in plain language. Never assume prior programming or biology background.
- **Ask before complex steps**: Confirm with me before running multi-step 
  or irreversible operations.
- **Coordinate System Validation**: Always explicitly verify whether 
  input files (BED, GFF, FASTA, etc.) use 0-based or 1-based coordinate 
  systems. Write validation checks to confirm alignment.
- **Python Execution & Environments**: Always run scripts using 
  `uv run python <script.py>` to ensure dependencies listed in 
  `pyproject.toml` are used. Never install packages globally with raw `pip`.
- **Counting & Math**: Never estimate sequence lengths, residue/token 
  counts, or metrics in a text response. Always write and run code to 
  compute these values.
- **Biological sanity checks**: Validate output against basic biological 
  invariants (e.g. proteins should start with M and end in a stop codon) 
  before presenting results as correct.
- **Error Handling**: If a library error occurs, check `pyproject.toml` 
  first, update with `uv add`, and retry rather than skipping the task.
