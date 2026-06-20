"""
Esercizio CLI bioinformatico — simulato con Python
====================================================
Questo script fa esattamente quello che farebbero i tool:
  - samtools  → conta le letture in un FASTQ
  - bcftools  → conta le varianti con filtro PASS in un VCF
  - bedtools  → calcola la sovrapposizione tra due file BED

Usiamo Python puro, senza installare nulla di extra.
"""

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# ─────────────────────────────────────────────────────────────
# ESERCIZIO 1 — Conta le letture in un file FASTQ
#   Equivalente CLI (Linux): grep -c "^@" sample.fastq
#   (su Linux si userebbe samtools view -c per i BAM,
#    ma il FASTQ è più semplice e non richiede samtools)
# ─────────────────────────────────────────────────────────────
def conta_reads_fastq(percorso_file: Path) -> int:
    """
    Un file FASTQ ha 4 righe per ogni lettura:
      riga 1: @nome_della_lettura   ← inizia con @
      riga 2: la sequenza di basi (A, T, C, G)
      riga 3: + (separatore)
      riga 4: qualità dei singoli nucleotidi

    Basta contare le righe che iniziano con @ per sapere
    quante letture ci sono nel file.
    """
    contenuto = percorso_file.read_text()
    righe_header = [r for r in contenuto.splitlines() if r.startswith("@")]
    return len(righe_header)


# ─────────────────────────────────────────────────────────────
# ESERCIZIO 2 — Conta le varianti PASS in un VCF
#   Equivalente CLI (Linux): bcftools view -f PASS -H sample.vcf | wc -l
# ─────────────────────────────────────────────────────────────
def conta_varianti_pass(percorso_file: Path) -> int:
    """
    Un file VCF ha:
      - righe di commento/header che iniziano con # (da ignorare)
      - righe dati: ogni colonna è separata da TAB
          col 0 = cromosoma
          col 1 = posizione
          col 6 = FILTER (es. PASS, LowQual)

    Contiamo solo le righe dove la colonna FILTER è "PASS".
    """
    count = 0
    for riga in percorso_file.read_text().splitlines():
        if riga.startswith("#"):   # intestazione → salta
            continue
        colonne = riga.split("\t")
        if len(colonne) >= 7 and colonne[6] == "PASS":
            count += 1
    return count


# ─────────────────────────────────────────────────────────────
# ESERCIZIO 3 — Sovrapposizione tra due file BED
#   Equivalente CLI (Linux): bedtools intersect -a a.bed -b b.bed -wo | awk ...
# ─────────────────────────────────────────────────────────────
def leggi_bed(percorso_file: Path) -> list[tuple]:
    """
    Un file BED ha almeno 3 colonne (tab-separated):
      col 0 = cromosoma  (es. chr1)
      col 1 = inizio     (0-based, cioè il primo nucleotide è 0)
      col 2 = fine       (esclusa, stile Python)

    NOTA COORDINATE: BED usa coordinate 0-based.
    Questo significa che la regione "chr1 100 200" copre
    i nucleotidi dalla posizione 100 (inclusa) alla 200 (esclusa),
    cioè 100 basi in totale.
    """
    regioni = []
    for riga in percorso_file.read_text().splitlines():
        if not riga.strip():
            continue
        parti = riga.split("\t")
        chrom, start, end = parti[0], int(parti[1]), int(parti[2])
        regioni.append((chrom, start, end))
    return regioni


def calcola_sovrapposizione(file_a: Path, file_b: Path) -> int:
    """
    Per ogni coppia di regioni (una da A, una da B) sullo stesso cromosoma,
    calcola quante basi paia si sovrappongono.

    Come funziona:
      regione A: [100 ──────── 300]
      regione B:       [180 ────────── 350]
      overlap:         [180 ── 300]   = 120 bp

      formula: overlap = max(0, min(fineA, fineB) - max(inizioA, inizioB))
    """
    regioni_a = leggi_bed(file_a)
    regioni_b = leggi_bed(file_b)

    totale_overlap = 0
    dettagli = []

    for (chromA, startA, endA) in regioni_a:
        for (chromB, startB, endB) in regioni_b:
            if chromA != chromB:
                continue  # cromosomi diversi → nessuna sovrapposizione possibile

            overlap = max(0, min(endA, endB) - max(startA, startB))
            if overlap > 0:
                totale_overlap += overlap
                dettagli.append(
                    f"  {chromA}:{startA}-{endA}  ∩  {chromA}:{startB}-{endB}  = {overlap} bp"
                )

    return totale_overlap, dettagli


# ─────────────────────────────────────────────────────────────
# MAIN — esegui i tre esercizi e mostra i risultati
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("ESERCIZIO 1 — Conta reads nel FASTQ (come samtools)")
    print("=" * 60)
    fastq = DATA_DIR / "sample.fastq"
    n_reads = conta_reads_fastq(fastq)
    print(f"File: {fastq.name}")
    print(f"Numero di letture (reads): {n_reads}")
    print()

    print("=" * 60)
    print("ESERCIZIO 2 — Conta varianti PASS nel VCF (come bcftools)")
    print("=" * 60)
    vcf = DATA_DIR / "sample.vcf"
    n_pass = conta_varianti_pass(vcf)
    # ── Controllo biologico (regola AGENTS.md) ──────────────
    tutte = sum(
        1 for r in vcf.read_text().splitlines()
        if r and not r.startswith("#")
    )
    assert n_pass <= tutte, "⚠️ Impossibile: più PASS che varianti totali!"
    # ────────────────────────────────────────────────────────
    print(f"File: {vcf.name}")
    print(f"Varianti totali: {tutte}")
    print(f"Varianti PASS:   {n_pass}")
    print(f"Varianti scartate (LowQual): {tutte - n_pass}")
    print(f"✅ Sanity check superato: {n_pass} ≤ {tutte}")
    print()

    print("=" * 60)
    print("ESERCIZIO 3 — Sovrapposizione BED (come bedtools intersect)")
    print("=" * 60)
    bed_a = DATA_DIR / "a.bed"
    bed_b = DATA_DIR / "b.bed"
    print("⚠️  NOTA COORDINATE: i file BED usano coordinate 0-based")
    print("   (es. '100 200' = posizioni 100,101,...,199 → 100 basi)")
    totale, dettagli = calcola_sovrapposizione(bed_a, bed_b)
    print(f"\nSovrapposizioni trovate:")
    for d in dettagli:
        print(d)
    print(f"\nTotale basi paia sovrapposte: {totale} bp")
