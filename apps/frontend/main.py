import streamlit as st 
import textwrap 
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.model import Ffeedback, Fimprove, Fviralità
from backend.utils import genera_percentuale




st.title("Rendi virali i tuoi tweets con AI")


tweet_prompt = st.text_area(label="", placeholder="Inserisci il tuo tweet", height=237)


if st.button("Invia"):
    if tweet_prompt == "":
        st.warning('La casella del tweet e vuota', icon="⚠️")
       
    else: 
        progress_text = "Analisi del tweet in corso...."
    
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        st.subheader("⭐ Rating", divider="gray")
        
        col1, col2 = st.columns(2)
        col1.metric(label="Possibilità di viralità (Attuale)", value=Fviralità(tweet_prompt), delta=genera_percentuale(), delta_color="inverse")
        col2.metric(label="Possibilità di viralità (Miglioranto)", value="10/10", delta="100%", delta_color="normal")

        st.subheader("✅ Feedback: ", divider="gray")
        container = st.container(border=True)
        container.write(f"{Ffeedback(tweet_prompt)}")

        st.subheader("🤖 Improved Tweet Improvement:", divider="gray")
        st.code(textwrap.fill(Fimprove(tweet_prompt), width=60), language="text")