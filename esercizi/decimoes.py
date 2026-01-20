'''10) Somma dei pari

Leggi N e calcola la somma dei numeri pari da 1 a N.'''

n = int(input("inserisci un intero:"))
pari = 0
for i in range(0, n+1):
    if i %2 == 0:
        pari += i

print(f"la somma dei numeri pari è {pari}")