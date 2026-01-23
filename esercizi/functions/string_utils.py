'''Modulo 4 — Stringhe (string_utils.py)


Obiettivo: lavorare con stringhe e caratteri




conta_caratteri(s) Restituisce la lunghezza della stringa



conta_lettera(s, lettera) Conta quante volte lettera appare in s



conta_vocali(s) Conta quante vocali ci sono nella stringa



is_palindromo(s) Restituisce True se la parola è palindroma



stampa_verticale(s) Stampa una lettera per riga'''





def conta_caratteri(s):
    return len(s)

#print(conta_caratteri("ciao"))



def conta_lettera(s, lettera):
    count = 0
    for i in s:
        if i == lettera:
            count += 1
    return count

#print(conta_lettera("ciaociao", "i"))


def conta_vocali(s):
    vocali = 0
    for c in s:
        if c == "a" or "e":
            vocali += 1
    return vocali
    

print(conta_vocali("ciaoof"))