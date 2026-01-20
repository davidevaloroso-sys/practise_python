'''Modulo 1 — Input e validazione (input_utils.py)


Obiettivo: imparare a leggere dati e controllarli

leggi_intero() Chiede un numero intero e lo restituisce, Se l’input non è valido, richiede di nuovo


leggi_intero_min_max(min, max) Restituisce un intero compreso tra min e max, Continua a chiedere finché il valore non è valido


leggi_float() Legge un numero decimale , Gestisce input errati


leggi_stringa_non_vuota() Chiede una stringa finché non è vuota'''

import random
import re

def leggi_intero():
    while True:
        s = input("inserisci un intero:")
        if s.startswith(("-" , "+")):#caso -ciao
            intero = s[1:].isdigit()
        else:
            intero = s.isdigit()#caso ciao quindi non parte con + o -
        if intero is True:
            return int(s)
        else:
            print("non hai inserito un intero valido, inserisci un intero valido per continuare:")

# ora chiamando questa funzione, potremmo assegnare il valore di ritorno ad una variabile ed utilizzarla in un'altro pezzo di codice.

#print(leggi_intero())



#leggi_intero_min_max(min, max) Restituisce un intero compreso tra min e max, Continua a chiedere finché il valore non è valido
#capire bene se sto coprendo tutti i casi
#vedi anche se la funzione random.ranint gestisce se inseriaamo ad esempio min = 10 e max -20. gestire se min è minore= del massimo.
def leggi_intero_min_max():
    while True:
        min = input("inserisci un minimo:")
        max = input("inserisci un massimo:")
        if min.startswith(( "-", "+" )):
            interomin = min[1:].isdigit()
        else:
            interomin = min.isdigit()
        if max.startswith(( "-" , "+" )):
            interomax = max[1:].isdigit()
        else:
            interomax= max.isdigit()
        if interomin and interomax is True and int(min) < int(max):
                numero = random.randint(int(min[0:]),int(max[0:]))
                return (numero)
        else:
            print("non hai inserito parametri MIN & MAX validi, reinserisci parametri validi!")

#leggi_intero_min_max()
#print(leggi_intero_min_max())




'''leggi_float() Legge un numero decimale , Gestisce input errati'''

#bisogna controllare tutti gli inserimenti, e assicurarci che il parametro inserito dall'utente contenga il .

def leggi_float():
    while True:
        put = input("inserisci un numero decimale es: 10.5 -->")
        if put.startswith(("-", "+")):
            dec = float(put)
            print(f"{dec} primo if")
        else:
            dec = put.isdecimal()
            print(f"{dec} secondo if")
        if dec is True:
            for c in put:
                print(c)
                if c == ".":
                    print("c'è il punto '.'")

leggi_float()




