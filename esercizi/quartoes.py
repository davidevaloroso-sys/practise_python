'''4) Sconto al negozio

Leggi prezzo (float) e stampa il prezzo finale:
se prezzo ≥ 100 → sconto 10%
altrimenti → nessuno sconto
 arrotonda a 2 decimali (con round())'''

print("calcolo dello sconto:")

prezzo = float(input("inserisci il prezzo:"))

if prezzo >= 100:
    sconto = float(prezzo) * 0.10
    #prezzo = prezzo - sconto
    prezzo = round(prezzo, 2)
else:
    print("non hai diritto a nessuno sconto")
prezzo = prezzo - sconto
print(f"il prezzo da pagare è: {prezzo}")