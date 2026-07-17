import sys
import time

def pi_ternario_infinito(base=3):
    """
    Generatore spigot universale con controllo dei limiti dinamico.
    """
    q, r, t, k, l = 1, 0, 1, 1, 3
    
    while True:
        n_lower = (3 * q + r) // t
        n_upper = (4 * q + r) // t
        
        if n_lower == n_upper:
            yield n_lower
            q = base * q
            r = base * (r - n_lower * t)
        else:
            q, r, t, k, l = (
                q * k,
                (2 * q + r) * l,
                t * l,
                k + 1,
                l + 2
            )

if __name__ == "__main__":
    # Definizione delle sequenze di escape ANSI per i colori
    # 91=Rosso brillante, 92=Verde brillante, 94=Blu brillante, 0=Reset
    COLORI = {
        0: "\033[91m",  # Rosso
        1: "\033[92m",  # Verde
        2: "\033[94m"   # Blu
    }
    RESET = "\033[0m"

    print("Calcolo rigoroso di Pi Greco in Base 3 a flusso continuo.")
    print("Premere CTRL+C per interrompere.\n")
    
    generatore = pi_ternario_infinito(base=3)
    
    prima_cifra = next(generatore)
    if prima_cifra == 3:
        # Formattiamo manualmente il "10" iniziale con i colori corretti
        # 1 è verde, 0 è rosso, il punto non ha colore
        sys.stdout.write(f"{COLORI[1]}1{COLORI[0]}0{RESET}.")
        sys.stdout.flush()
    
    try:
        for cifra in generatore:
            # Estrae il colore corrispondente, stampa la cifra e resetta subito il terminale
            colore_ansi = COLORI.get(cifra, "")
            sys.stdout.write(f"{colore_ansi}{cifra}{RESET}")
            sys.stdout.flush()
            
    except KeyboardInterrupt:
        # Inseriamo il RESET anche qui per evitare che il prompt della shell 
        # erediti accidentalmente l'ultimo colore stampato
        print(f"{RESET}\n\nProcesso terminato correttamente.")
