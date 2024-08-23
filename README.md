# Twitter AI Analyzer

**Twitter AI Analyzer** è una web app interattiva progettata per aiutare gli utenti a ottimizzare i loro tweet e massimizzare la loro viralità. Con la crescente competizione sui social media, può essere difficile capire quali contenuti hanno il potenziale per attirare l'attenzione e generare coinvolgimento. Questa applicazione utilizza l'intelligenza artificiale per affrontare questo problema in tre modi principali:

1. **Valutazione della Viralità**: Fornisce una valutazione dettagliata della probabilità che un tweet diventi virale, aiutando gli utenti a comprendere l'efficacia del loro contenuto.

2. **Feedback Costruttivo**: Offre feedback mirato sui tweet, suggerendo aree di miglioramento per aumentare l'attrattiva e il coinvolgimento del pubblico.

3. **Ottimizzazione del Contenuto**: Genera versioni migliorate del tweet originale, ottimizzate per ottenere il massimo impatto e attrattiva, basate su pratiche e trend di successo.

Con **Twitter AI Analyzer**, gli utenti possono ottenere intuizioni preziose e suggerimenti pratici per migliorare le loro strategie sui social media, risparmiando tempo e aumentando l'efficacia dei loro tweet.

## Struttura del Progetto

Il progetto è organizzato come segue:

 ```bash
Twitter AI Analyzer/
│
├── backend/
│ ├── init.py
│ ├── model.py
│ └── utils.py
│
├── design/
│ ├── Sequence Diagram.pn
│ └── System Diagram.pn
│
├── frontend/
│ ├── .streamlit/
│ │ └── config.toml
│ ├── init.py
│ └── main.py
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
 ```

## Installazione

Segui questi passaggi per configurare il progetto:

1. **Clona il Repository**

   ```bash
   git clone https://github.com/tuo-utente/twitter-ai-analyzer.git
   cd twitter-ai-analyzer

2. **Crea e Attiva un Ambiente Virtuale**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`

3. **Installa le Dipendenze**
   Assicurati di avere il file requirements.txt nella directory principale e installa tutte le dipendenze necessarie:
   ```bash
   pip install -r requirements.txt

4. **Configura le Variabili d'Ambiente**
   Crea un file .env nella directory principale e aggiungi le variabili d'ambiente necessarie. Assicurati di seguire il formato del file .env che puoi trovare nel repository o     chiedere al team di sviluppo.

5. **Esegui l'Applicazione**
   ```bash
   streamlit run frontend/main.py

## Utilizzo

1. **Accedi all'Applicazione**

   Dopo aver avviato l'applicazione, apri un browser web e vai all'indirizzo [http://localhost:8501](http://localhost:8501).

2. **Inserisci il Tweet**

   - Nella pagina principale, troverai un'area di testo con l'etichetta "Inserisci il tuo tweet".
   - Digita o incolla il testo del tweet che desideri analizzare.

3. **Analizza il Tweet**

   - Clicca sul pulsante **"Invia"** per avviare l'analisi del tweet.
   - Durante l'elaborazione, verrà mostrata una barra di progresso che indica il progresso dell'analisi.

4. **Visualizza i Risultati**

   Dopo che l'analisi è completata, vedrai diverse sezioni con i seguenti risultati:
   
   - **⭐ Rating**:
     - **Possibilità di viralità (Attuale)**: Mostra una valutazione numerica della probabilità che il tweet diventi virale, calcolata utilizzando il modello AI.
     - **Possibilità di viralità (Migliorato)**: Mostra una valutazione ideale di viralità, impostata a "10/10" come riferimento per il miglioramento.

   - **✅ Feedback**:
     - Fornisce un feedback dettagliato sul tweet, evidenziando i punti di forza e le aree di miglioramento. Questo feedback è progettato per aiutarti a rendere il tweet più coinvolgente e rilevante.

   - **🤖 Improved Tweet Improvement**:
     - Mostra una versione migliorata del tweet originale. Questo tweet è ottimizzato per ottenere una maggiore viralità e coinvolgimento, basato sui suggerimenti del modello AI.

5. **Rivedi e Adatta**

   - Puoi utilizzare i risultati e il feedback per modificare il tuo tweet e testare ulteriormente la sua efficacia.
   - Inserisci nuovamente il tweet modificato nell'area di testo e ripeti il processo per continuare a migliorare la qualità del contenuto.

## Struttura del Codice

Il progetto è suddiviso in tre principali directory: `backend`, `frontend`, e `design`. Di seguito è riportata una panoramica di ciascuna directory e dei suoi componenti principali.

### `backend/`

Questa directory contiene il codice che gestisce l'elaborazione e l'analisi dei tweet.

- **`__init__.py`**: File di inizializzazione del modulo `backend`.
- **`model.py`**: Contiene le funzioni per analizzare e migliorare i tweet:
  - `Ffeedback(tweet_prompt)`: Fornisce feedback costruttivo sul tweet.
  - `Fimprove(tweet_prompt)`: Genera una versione migliorata del tweet.
  - `Fviralità(tweet_prompt)`: Valuta la probabilità di viralità del tweet.
- **`utils.py`**: Contiene utilità generali come:
  - `genera_percentuale()`: Genera una percentuale casuale tra 5 e 50%.

### `frontend/`

Questa directory contiene il codice per l'interfaccia utente basata su Streamlit.

- **`__init__.py`**: File di inizializzazione del modulo `frontend`.
- **`main.py`**: Il file principale che definisce l'interfaccia utente dell'applicazione. Utilizza Streamlit per creare l'interfaccia web interattiva.
- **`.streamlit/config.toml`**: File di configurazione per Streamlit. Imposta le opzioni di configurazione per l'applicazione.

### `design/`

Questa directory contiene i diagrammi di progettazione del sistema.

- **`Sequence Diagram.pn`**: Diagramma di sequenza che mostra le interazioni tra i componenti del sistema.
- **`System Diagram.pn`**: Diagramma del sistema che fornisce una panoramica dell'architettura complessiva del progetto.

## Diagrammi

Trovi i diagrammi di sequenza e del sistema nella cartella `design/`:

- **[Sequence Diagram.png](design/Sequence%20Diagram..png)**: Mostra la sequenza delle interazioni tra i componenti del sistema, evidenziando come i dati e le richieste si spostano attraverso il sistema durante l'elaborazione del tweet.
- **[System Diagram.png](design/System%20Diagram..png)**: Fornisce una panoramica dell'architettura complessiva del sistema, visualizzando i principali componenti e le loro interazioni.

## Requisiti

Per eseguire **Twitter AI Analyzer**, assicurati di avere i seguenti requisiti:

### Software

- **Python**: Versione 3.7 o superiore

### Pacchetti Python

Installa le dipendenze necessarie utilizzando il file `requirements.txt`. Esegui il comando seguente per installare tutti i pacchetti richiesti:

```bash
 pip install -r requirements.txt
```
### Pacchetti Principali

Il file `requirements.txt` include i seguenti pacchetti principali:

- **`streamlit`**: Per creare l'interfaccia utente web.
- **`langchain_google_genai`**: Per l'integrazione con i modelli generativi AI di Google.
- **`langchain_core`**: Per la gestione dei messaggi e delle interazioni con l'AI.
- **`python-dotenv`**: Per gestire le variabili d'ambiente.

### Variabili d'Ambiente

Crea un file `.env` nella directory principale del progetto e aggiungi le seguenti variabili d'ambiente necessarie:

- **`GOOGLE_API_KEY`**: La chiave API per l'accesso ai modelli AI di Google.
- **Altre variabili**: Eventuali altre configurazioni specifiche per il tuo ambiente.

Assicurati che le variabili d'ambiente siano configurate correttamente per l'esecuzione dell'applicazione.

## Contribuire

Contributi sono benvenuti! Per contribuire al progetto, segui questi passaggi:

1. **Fork il repository**: Crea una copia del repository nel tuo account GitHub.
2. **Crea un branch per le tue modifiche**: Nella tua copia del repository, crea un nuovo branch per lavorare sulle tue modifiche.
3. **Invia una pull request**: Una volta completate le modifiche, invia una pull request al repository originale con una descrizione dettagliata delle modifiche che hai apportato.

Grazie per il tuo interesse e contributo al progetto!

## Licenza

Questo progetto è concesso in licenza con la [MIT License](LICENSE).

## Contatti

Per qualsiasi domanda o supporto, contatta [Linkedln](mailto:https://www.linkedin.com/in/razak-hamidu).

