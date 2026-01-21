'''Modulo 3 — Cicli e contatori (loop_utils.py)


Obiettivo: padroneggiare for e while




somma_da_1_a_n(n) Somma dei numeri da 1 a n



somma_pari_fino_a_n(n) Somma solo i numeri pari



conta_fino_a(n) Stampa i numeri da 1 a n



conto_alla_rovescia(n) Stampa da n a 0






conta_divisibili(n, divisore) Conta quanti numeri da 1 a n sono divisibili per divisore'''


def somma_da_1_a_n(n):
    c = 0
    for i in range(1, n+1):
        c = i + c
    return c
    

def somma_pari_fino_a_n(n):
    c = 0
    for i in range(n+1):
        if i % 2 == 0:
            c = i + c
    return c

def conta_fino_a_n(n):
    for i in range(n+1):
        print(i)


def conto_alla_rovescia(n):
    for i in range(0, n+1):
        print(n - i)

'''conta_divisibili(n, divisore) Conta quanti numeri da 1 a n sono divisibili per divisore'''

#si divide n per il divisore e si considerano solo i numeri che sono multipli del divisore, per ottenere il numero dei multipli quindi divisibili per il divisore si procede con d / d
def conta_divisibili(n , divisore):
    count = 0
    for i in range(1, n+1):
        if i % divisore == 0:
            count += 1
    return count
        
print(conta_divisibili(10, 5))
        
    
    
