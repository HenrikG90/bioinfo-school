"""
Questo script legge un file FASTA e stampa, per ogni sequenza:
- il nome
- la lunghezza (numero di basi)
- la percentuale di GC (basi G e C, importante in biologia molecolare)
"""

import os  # os è più familiare di pathlib per i principianti


# --- Funzione 1: legge il file FASTA ---
def leggi_fasta(percorso_file):
    """
    Legge un file FASTA e restituisce un dizionario:
        { "nome_sequenza": "ATCGATCG..." }
    """
    sequenze = {}          # dizionario vuoto che riempiremo
    nome_corrente = None   # il nome dell'ultima sequenza trovata (parte dopo '>')
    basi_correnti = []     # lista delle righe di basi per la sequenza corrente

    with open(percorso_file) as file:
        for riga in file:
            riga = riga.strip()  # rimuovi spazi e '\n' a inizio/fine riga

            if riga.startswith(">"):
                # Siamo su una riga di intestazione (es. ">nome_sequenza")
                # Prima di passare alla nuova sequenza, salva quella precedente
                if nome_corrente is not None:
                    sequenze[nome_corrente] = "".join(basi_correnti)

                # Prendi il nome (tutto dopo il '>')
                nome_corrente = riga[1:]
                basi_correnti = []  # reset per la nuova sequenza

            else:
                # Riga di basi (es. "ATCGATCG")
                basi_correnti.append(riga)

    # Salva l'ultima sequenza (non ne incontra un'altra dopo!)
    if nome_corrente is not None:
        sequenze[nome_corrente] = "".join(basi_correnti)

    return sequenze


# --- Funzione 2: calcola la percentuale GC ---
def calcola_gc(sequenza):
    """
    Calcola la percentuale di basi G e C nella sequenza.
    Restituisce un numero tra 0.0 e 1.0
    """
    if len(sequenza) == 0:  # evita divisione per zero
        return 0.0

    numero_g = sequenza.count("G")
    numero_c = sequenza.count("C")
    totale_gc = numero_g + numero_c

    return totale_gc / len(sequenza)


# --- Funzione principale ---
def main():
    # Costruisce il percorso di example.fa nella stessa cartella dello script
    cartella_script = os.path.dirname(os.path.abspath(__file__))
    percorso_file = os.path.join(cartella_script, "example.fa")

    # Leggi tutte le sequenze dal file
    sequenze = leggi_fasta(percorso_file)

    # Stampa i risultati
    print("Nome\t\tLunghezza\t%GC")
    print("-" * 40)

    for nome, sequenza in sequenze.items():
        lunghezza = len(sequenza)
        gc = calcola_gc(sequenza)
        print(f"{nome}\t{lunghezza}\t{gc:.1%}")  # es. "87.5%"


if __name__ == "__main__":
    main()
