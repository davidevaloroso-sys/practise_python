'''9) Tabellina

Leggi n e stampa n x 1 … n x 10.
fai scegliere anche da quale a quale (es. 1..20).'''


n = int(input("inserisci un numero"))

min = int(input("inserisci il numero di partenza:"))
max = int(input("inserisci il numero di fine:"))

for i in range(min, max+1):
    print(f" {n} * {i} = {n * i}")
