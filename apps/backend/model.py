from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
)


tweet_example = "🌞 Buongiorno a tutti! Oggi è una giornata perfetta per una passeggiata all'aria aperta. 🏞️ Non dimenticate di prendere un po' di tempo per voi stessi e godervi la natura! 🌳✨ #Buongiorno #Relax #VivereBene"

def Fviralità(tweet_prompt):
    global viralità_r
    viralità = [
        SystemMessage(content="Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel capire e valutare la possibilità che vada virale un Twitter. Dammi una valutazione di viralità da 1 a 10. Dammi solo il numero di valutazione non rispondere con altri informazioni. Ecco il mio tweet"),
        HumanMessage(content=tweet_example),
        AIMessage(content="4/10"),
        HumanMessage(content=tweet_prompt)
    ]
    viralità_r = model.invoke(viralità).content 
    return viralità_r



######################################################


def Ffeedback(tweet_prompt):
    feedback =  [
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel dare feedback ai i Twitter. ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} e tu mi dirai un feedback testuale. Non darmi delle tweet migliorati o valutazione tue. Dammi sono un feedback testuale"), 
        HumanMessage(content=tweet_example), 
        AIMessage(content="Il tweet ha un messaggio positivo e incoraggiante, che può risuonare bene con chi cerca ispirazione per la giornata. Tuttavia, potrebbe non avere un impatto virale elevato poiché è piuttosto generico e privo di elementi distintivi o di attualità. Per aumentare la probabilità di viralità, potresti considerare di aggiungere un elemento personale, una storia breve o una domanda che stimoli la partecipazione degli utenti. Inoltre, l'uso di hashtag è corretto, ma una combinazione di hashtag più mirati o di tendenze attuali potrebbe aiutare a raggiungere un pubblico più ampio."),
        HumanMessage(content=tweet_prompt)
    ]
    feedback_r = model.invoke(feedback).content
    return feedback_r



######################################################

def Fimprove(tweet_prompt):
    improve = [
        SystemMessage(content=f"Agisci come un Twitter AI Analyzer. Hai 10 anni di esperienza nel generale dei Twitter con viralità 10/10 . ti Daro un tweet che ha una probabilità di andare virale di {viralità_r} lo rigenerai e tu mi dirai Twitter con viralità 10/10 . Non dammi altre spiegazione o informazione ulteriori. Dammi sono il Twitter con ricreato con  con viralità 10/10 "),
        HumanMessage(content=tweet_example),
        AIMessage(content="🌟 Buongiorno, Twitter! 🌟 Oggi è il giorno ideale per una passeggiata nella natura e un po' di tempo per te stesso! 🚶‍♂️🌳 Prenditi una pausa, respira profondamente e ricarica le energie. 💚✨ #ViviAlMassimo #Natura #SelfCare"),
        HumanMessage(content=tweet_prompt)

    ]
    improve_r = model.invoke(improve).content
    return improve_r










        