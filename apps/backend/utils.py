import random

def genera_percentuale():
    # Genera un numero casuale tra 5 e 50
    percentuale = random.uniform(5, 50)
    # Arrotonda il risultato a due decimali per ottenere una percentuale con due cifre decimali
    return f"{round(percentuale, 2)}%"""