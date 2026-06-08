"""
Reads genome.fa and annotations.gff3, extracts the nucleotide sequence of
each CDS, translates it to protein, and prints:

    gene_name<TAB>nt_sequence<TAB>protein_sequence

COORDINATE SYSTEM NOTE:
  GFF3 uses 1-based, inclusive coordinates: [start, end]
  Python slicing uses 0-based, exclusive end:  seq[start-1 : end]
  Getting this wrong silently drops the first base of every CDS.
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Standard genetic code: codon -> single-letter amino acid ("*" = stop)
CODON_TABLE = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def read_fasta(path):
    """Return a dict {chrom_name: sequence_string} from a FASTA file."""
    sequences = {}
    name, parts = None, []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name:
                    sequences[name] = "".join(parts)
                name = line[1:].split()[0]  # take only the first word as ID
                parts = []
            else:
                parts.append(line)
    if name:
        sequences[name] = "".join(parts)
    return sequences


def parse_gff3(path, feature_type="CDS"):
    """
    Return a list of dicts for all rows of the given feature_type.
    Each dict has: chrom, start (1-based), end (1-based, inclusive),
                   strand, and attributes as a dict.
    """
    features = []
    with open(path) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            cols = line.strip().split("\t")
            if len(cols) < 9 or cols[2] != feature_type:
                continue
            attrs = {}
            for item in cols[8].split(";"):
                if "=" in item:
                    key, val = item.split("=", 1)
                    attrs[key.strip()] = val.strip()
            features.append({
                "chrom":  cols[0],
                "start":  int(cols[3]),   # GFF3: 1-based
                "end":    int(cols[4]),   # GFF3: inclusive
                "strand": cols[6],
                "attrs":  attrs,
            })
    return features


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    complement = str.maketrans("ACGTacgt", "TGCAtgca")
    return seq.translate(complement)[::-1]


def translate(nt_seq):
    """
    Translate a nucleotide sequence to protein using the standard genetic code.
    Stops at the first stop codon (not included in output).
    """
    protein = []
    for i in range(0, len(nt_seq) - 2, 3):
        codon = nt_seq[i:i+3].upper()
        aa = CODON_TABLE.get(codon, "?")
        if aa == "*":
            break
        protein.append(aa)
    return "".join(protein)


def main():
    genome   = read_fasta(os.path.join(SCRIPT_DIR, "genome.fa"))
    features = parse_gff3(os.path.join(SCRIPT_DIR, "annotations.gff3"))

    for feat in features:
        chrom  = feat["chrom"]
        start  = feat["start"]   # 1-based
        end    = feat["end"]     # 1-based, inclusive
        strand = feat["strand"]
        name   = feat["attrs"].get("Name", feat["attrs"].get("ID", "unknown"))

        chrom_seq = genome.get(chrom, "")

        # KEY CONVERSION: GFF3 [start, end] -> Python [start-1, end]
        nt_seq = chrom_seq[start - 1 : end]

        if strand == "-":
            nt_seq = reverse_complement(nt_seq)

        protein = translate(nt_seq)

        print(f"{name}\t{nt_seq}\t{protein}")


if __name__ == "__main__":
    main()
