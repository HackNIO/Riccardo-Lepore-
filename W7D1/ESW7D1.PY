def lunghezze_parole():
    # Chiede all'utente di inserire le parole separandole con uno spazio
    parole_input = input("Inserisci le parole separate da uno spazio: ")
    
    # Suddivide la stringa di input in una lista di parole
    lista_parole = parole_input.split()
    
    # Crea una lista vuota per memorizzare le lunghezze delle parole
    lunghezze = []
    
    # Itera attraverso ogni parola nella lista di input
    for parola in lista_parole:
        # Aggiunge la lunghezza della parola alla lista delle lunghezze
        lunghezze.append(len(parola))
    
    # Restituisce la lista delle lunghezze
    return lunghezze

# Esempio di utilizzo
B = lunghezze_parole()
print("Le lunghezze delle parole inserite sono:", B)