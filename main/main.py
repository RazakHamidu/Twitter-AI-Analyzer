from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st 
import textwrap 
import random



from streamlit_extras.stylable_container import stylable_container

with open("C:\\Users\\Razak\\Desktop\\Twitter AI Analyzer\\main\pino.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_dotenv()

st.title("Rendi virali i tuoi tweets con AI")

model = ChatOpenAI(model="gpt-4o-mini") 



tweet_prompt = st.text_area(label="", placeholder="Inserisci il tuo tweet", height=237)


viralità = [
    SystemMessage(content="Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel capire e valutare la possibilità che vada virale un Twitter. Dammi una valutazione di viralità da 1 a 10. Dammi solo il numero di valutazione non rispondere con altri informazioni. Ecco il mio tweet"),
    HumanMessage(content="🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"),
    AIMessage(content="4/10"),
    HumanMessage(content=tweet_prompt)
]




viralità_r = model.invoke(viralità).content


######################################################



feedback =  [
    SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel dare feedback ai i Twitter. ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} e tu mi dirai un feedback testuale. Non darmi delle tweet migliorati o valutazione tue. Dammi sono un feedback testuale"), 
    HumanMessage(content="🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"), 
    AIMessage(content="Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio."),
    HumanMessage(content=tweet_prompt)
]


feedback_r = model.invoke(feedback).content




######################################################


improve = [
    SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel generale dei Twitter con viralità 10/10 . ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} lo rigenerai e tu mi dirai Twitter con viralità 10/10 . Non dammi altre spiegazione o informazione ulteriori. Dammi sono il Twitter con ricreato con  con viralità 10/10 "),
    HumanMessage(content="🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"),
    AIMessage(content="🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"),
    HumanMessage(content=tweet_prompt)

]

improve_r = model.invoke(improve).content





# image section 

def genera_percentuale():
    # Genera un numero casuale tra 5 e 50
    percentuale = random.uniform(5, 50)
    # Arrotonda il risultato a due decimali per ottenere una percentuale con due cifre decimali
    return f"{round(percentuale, 2)}%"

if st.button("Invia"):

    
    st.subheader("⭐ Rating", divider="gray")
    
    col1, col2 = st.columns(2)
    col1.metric(label="Possibilità di viralità (Attuale)", value=viralità_r, delta=genera_percentuale(), delta_color="inverse")
    col2.metric(label="Possibilità di viralità (Miglioranto)", value="10/10", delta="100%", delta_color="normal")

    st.subheader("✅ Feedback: ", divider="gray")
    container = st.container(border=True)
    container.write(f"{feedback_r}")

    st.subheader("🤖 Improved Tweet Improvement:", divider="gray")
    st.code(textwrap.fill(improve_r, width=60), language="text")


# todo: - Migliorare il out section 
# todo: - Aggiugere la barra di progressione
# todo: - Aggiugere  La Metrica di viralità
# todo: Aggiugere il color pallate di x e font 
