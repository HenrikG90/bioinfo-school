# Esercitazione: Le 3 Modalità di Interazione Agente-Strumento

Per comprendere a fondo la differenza tra le tre modalità descritte in [week4.md](file:///c:/Users/enric/bioinfo-school/weeks/week4.md), useremo il file FASTA d'esempio [example.fa](file:///c:/Users/enric/bioinfo-school/exercises/week2/example.fa).

L'obiettivo è: **Contare il numero di sequenze nel file FASTA** (ossia quante righe iniziano con `>`).

---

### Modo 1: L'agente scrive codice che chiama lo strumento (Approccio Riproducibile)
In questa modalità, l'agente genera uno script Python riutilizzabile e lo esegue (o lo fa eseguire a te).

#### Come provarlo:
1. Crea un file chiamato `count_fasta_mode1.py` con questo codice:
   ```python
   # count_fasta_mode1.py
   with open("exercises/week2/example.fa", "r") as f:
       lines = f.readlines()
   
   headers = [line for line in lines if line.startswith(">")]
   print(f"Numero di sequenze: {len(headers)}")
   ```
2. Esegui lo script dal terminale:
   ```bash
   uv run python count_fasta_mode1.py
   ```
* **Vantaggio:** Il codice è salvato, versionato su Git, e chiunque può riprodurre l'analisi esattamente nello stesso modo.

---

### Modo 2: L'agente esegue direttamente i comandi (Approccio Esplorativo Estemporaneo)
In questa modalità, l'agente (o tu direttamente) digita un comando rapido nel terminale senza creare file di script persistenti.

#### Come provarlo (usando PowerShell su Windows):
Esegui questo comando direttamente nel terminale:
```powershell
Select-String -Path .\exercises\week2\example.fa -Pattern "^>" | Measure-Object | Select-Object -ExpandProperty Count
```
Oppure usando un comando Python "one-liner":
```powershell
python -c "print(open('exercises/week2/example.fa').read().count('>'))"
```
* **Vantaggio:** È velocissimo per risposte al volo ("ad-hoc").
* **Svantaggio:** Non lascia traccia o script riutilizzabili nel codice sorgente. Se qualcun altro clona il tuo repository, non saprà come hai ottenuto quel numero.

---

### Modo 3: L'agente chiama strumenti strutturati (MCP / Function Calling)
In questa modalità, l'agente non scrive codice personalizzato e non scrive comandi generici da terminale. Utilizza invece degli strumenti predefiniti messi a disposizione dall'IDE o da un server esterno (chiamato MCP Server). I parametri vengono passati come un oggetto JSON strutturato e l'output viene restituito in modo altrettanto strutturato.

#### Come provarlo ora con me (Antigravity):
Chiedimi di trovare le righe che iniziano con `>` nel file `exercises/week2/example.fa` usando il mio strumento di ricerca. 

Ad esempio, puoi scrivermi in chat:
> *"Usa lo strumento grep_search per contare quanti record ci sono in exercises/week2/example.fa"*

Io non scriverò script Python e non userò il terminale di Windows: chiamerò direttamente la funzione `grep_search` (che è a tutti gli effetti una chiamata di tipo Mode 3).
