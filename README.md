# Pi Greco in Base 3 (Ternario) 🔴🟢🔵

Un calcolatore infinito a flusso continuo delle cifre di Pi Greco nel sistema di numerazione ternario (Base 3), scritto in Python puro senza dipendenze esterne.

## Il Problema Matematico
Gli algoritmi *spigot* tradizionali (come quello di Rabinowitz-Wagon o la variante di Gibbons) sono hardcoded per convergere in base 10, basandosi su limiti di guardia fissi per l'estrazione delle cifre. Forzare questi algoritmi in basi diverse porta a instabilità, overflow e generazione di cifre negative.

## La Soluzione
Questo script utilizza l'algoritmo di Spigot generalizzato con **controllo dinamico dei limiti**. Calcolando il limite inferiore e superiore della frazione continua iterazione per iterazione, il programma estrae il *trit* (cifra ternaria) solo quando i due limiti collassano sullo stesso intero, garantendo una stabilità matematica assoluta per qualsiasi base.

## Caratteristiche
- **Flusso infinito:** Nessun accumulo in memoria (RAM footprint costante). Usa un generatore `yield`.
- **Rendering ANSI:** Colora l'output direttamente nel terminale bypassando le librerie di sistema.
  - `0` = Rosso
  - `1` = Verde
  - `2` = Blu

## Esecuzione
```bash
python3 pi_ternario.py
