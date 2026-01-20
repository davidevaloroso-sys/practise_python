'''5) Somma finché non scrivo 0

Continua a chiedere numeri e somma tutto.

Quando l’utente inserisce 0, stampa la somma totale.
conta quanti numeri validi sono stati inseriti (escludi lo zero finale)'''

numero = int(input("inserisci un numero, quando vuoi stoppare inserisci 0:"))
somma = 0
val = 0
while numero != 0:
    somma+=numero
    val += 1
    numero = int(input("inserisci un numero, quando vuoi stoppare inserisci 0:"))
print(f"la somma dei numeri inseriti è: {somma}")

print(f"i numeri inseriti validi diversi da 0 sono:{val}")