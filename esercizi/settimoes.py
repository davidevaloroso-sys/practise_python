'''7) Numero in range (validazione)

Chiedi un numero intero .

Se è fuori range, richiedilo con un messaggio.

Quando è valido: stampa “OK”.'''

numero = int(input("inserisci un numero intero:"))

for num in range(0, 10):
    if numero >=11:
        print("non hai inserito un numero intero nel range!")
        numero = int(input("inserisci un numero intero:"))
else:
    print("ok")
