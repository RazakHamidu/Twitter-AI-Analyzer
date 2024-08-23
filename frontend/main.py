# Importa la libreria Streamlit per creare l'interfaccia utente web
import streamlit as st 

# Importa il modulo textwrap per formattare il testo
import textwrap 

# Importa il modulo time per gestire i ritardi e la visualizzazione dei progressi
import time

# Importa i moduli sys e os per la gestione del percorso e delle variabili di ambiente
import sys
import os

# Aggiunge il percorso della directory padre al percorso di ricerca dei moduli
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa le funzioni dal modulo backend.model
from backend.model import Ffeedback, Fimprove, Fviralità

# Importa la funzione genera_percentuale dal modulo backend.utils
from backend.utils import genera_percentuale

# Imposta il titolo dell'applicazione Streamlit
st.title("Rendi virali i tuoi tweets con AI")

# Crea un'area di testo dove l'utente può inserire il tweet
tweet_prompt = st.text_area(label="", placeholder="Inserisci il tuo tweet", height=237)

# Crea un pulsante "Invia" che attiva l'analisi del tweet
if st.button("Invia"):
    # Controlla se il campo di testo è vuoto
    if tweet_prompt == "":
        # Mostra un avviso se il campo di testo è vuoto
        st.warning('La casella del tweet e vuota', icon="⚠️")
       
    else:
        # Testo per la barra di progresso
        progress_text = "Analisi del tweet in corso...."
    
        # Crea una barra di progresso e aggiorna il suo stato
        my_bar = st.progress(0, text=progress_text)

        # Aggiorna la barra di progresso da 0 a 100%
        for percent_complete in range(100):
            time.sleep(0.01)  # Pausa per simulare l'elaborazione
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        # Attendere un secondo prima di svuotare la barra di progresso
        time.sleep(1)
        my_bar.empty()

        # Sezione per visualizzare il punteggio di viralità
        st.subheader("⭐ Rating", divider="gray")
        
        # Crea due colonne per visualizzare il punteggio di viralità attuale e migliorato
        col1, col2 = st.columns(2)
        col1.metric(
            label="Possibilità di viralità (Attuale)", 
            value=Fviralità(tweet_prompt),  # Calcola il punteggio di viralità attuale
            delta=genera_percentuale(),  # Genera una percentuale di variazione casuale
            delta_color="inverse"
        )
        col2.metric(
            label="Possibilità di viralità (Migliorato)", 
            value="10/10",  # Punteggio migliorato fisso
            delta="100%",  # Delta fisso al 100%
            delta_color="normal"
        )

        # Sezione per visualizzare il feedback sul tweet
        st.subheader("✅ Feedback: ", divider="gray")
        container = st.container(border=True)
        container.write(f"{Ffeedback(tweet_prompt)}")  # Mostra il feedback ricevuto dalla funzione Ffeedback

        # Sezione per visualizzare il tweet migliorato
        st.subheader("🤖 Improved Tweet Improvement:", divider="gray")
        st.code(
            textwrap.fill(Fimprove(tweet_prompt), width=60),  # Mostra il tweet migliorato con formattazione
            language="text"
        )