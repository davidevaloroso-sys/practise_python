#Modulo 2 — Operazioni matematiche (math_utils.py)

#Obiettivo: usare parametri e valori di ritorno


'''somma(a, b)



differenza(a, b)



prodotto(a, b)



divisione(a, b) Se b == 0, restituisce None



media(a, b) Restituisce la media di due numeri



is_pari(n) Restituisce True se n è pari, altrimenti False'''



def somma(a, b):
    return a + b


def differenza(a, b):
    return a - b


def prodotto(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return None
    else:
        return a / b

print(divisione(3, 2))


def media(a, b):
    return (a + b) / 2


def is_pari(n):
    return n % 2 == 0
        

    




        
    