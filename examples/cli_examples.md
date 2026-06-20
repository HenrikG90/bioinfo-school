# Esempi di CLI bioinformatici

Questo file mostra, in modo semplice e commentato, come utilizzare alcuni dei più comuni **tool da riga di comando** in bioinformatica.

---
## 1. `samtools` – contare le letture in un BAM
```bash
# Conta le letture allineate al cromosoma 21
samtools view -c sample.bam chr21
```
- `view` apre il BAM.
- `-c` stampa solo il numero di reads.
- `chr21` limita l'analisi al cromosoma 21.

---
## 2. `bcftools` – contare le varianti filtrate "PASS"
```bash
# Numero di varianti con filtro PASS in un VCF
bcftools view -f PASS -H sample.vcf | wc -l
```
- `-f PASS` seleziona solo record con filtro PASS.
- `-H` rimuove l'header del VCF.
- `wc -l` conta le righe rimanenti.

---
## 3. `bedtools intersect` – sovrapposizione di regioni BED
```bash
# Calcola la sovrapposizione totale (in bp) tra due BED
bedtools intersect -a a.bed -b b.bed -wo \
  | awk '{sum+=$7} END{print sum}'
```
- `-a` e `-b` sono i due file BED.
- `-wo` (write‑overlap) stampa la lunghezza di ogni overlap nella colonna 7.
- `awk` somma tutte le lunghezze.

---
## 4. `head` – estrarre le prime *n* letture da un FASTQ
```bash
# Prendi le prime 100 letture (2 linee per lettura) da un FASTQ
head -n 200 sample.fastq > first_100_reads.fastq
```
Un file FASTQ ha 4 linee per lettura; per 100 letture servono 400 linee, ma se il file contiene solo la sequenza e il nome (2 linee) useremo `-n 200`.

---
## 5. `samtools faidx` + `awk` – GC‑content di una regione FASTA
```bash
# Calcola il GC% nella regione chr1:1000‑2000
samtools faidx ref.fa chr1:1000-2000 | \
  awk 'BEGIN{gc=0; len=0} \
       $0!~/>/ {gsub(/[^GC]/,"",$0); gc+=length($0); len+=length($0)} \
       END{if(len>0) printf "GC%%: %.2f\n", (gc/len)*100}'
```
- `faidx` estrae la sequenza.
- `awk` conta le G e C e calcola la percentuale.

---
### Come usarli
1. Salva il file con estensione `.md` (es. `cli_examples.md`).
2. Apri un terminale nella cartella del tuo progetto.
3. Sostituisci i nomi dei file (`sample.bam`, `sample.vcf`, ecc.) con i tuoi.
4. Copia‑incolla il comando e premi `Invio`.

Questi esempi coprono operazioni di **conteggio**, **filtraggio**, **intersezione di regioni** e **analisi di composizione** – le funzioni più frequenti nelle pipeline bioinformatiche.
