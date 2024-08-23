# Importa il modulo random per generare numeri casuali
import random

# Definisce la funzione `genera_percentuale` che genera una percentuale casuale
def genera_percentuale():
    # Genera un numero casuale decimale tra 5 e 50
    percentuale = random.uniform(5, 50)
    
    # Arrotonda il numero generato a due decimali e formatta il risultato come stringa con il simbolo '%'
    # La funzione `round` arrotonda il numero a due cifre decimali
    # La funzione `f"{...}%"` converte il numero in una stringa e aggiunge il simbolo '%' alla fine
    return f"{round(percentuale, 2)}%"
