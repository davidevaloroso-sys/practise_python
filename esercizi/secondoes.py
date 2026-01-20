#leggi due numeri e applica operatori
print("Inserisci due numeri che verranno elaborati e ne sarà restituta la somma, differenza, prodotto e la divisione")
a = float(input("inserisci un float o intero:"))
b = float(input("inserisci un float o intero:"))

somma = a + b
print(f"la somma è {somma}")

differenza = a - b
print(f"la differenza è {differenza}")

prodotto = a * b
print(f"il prodotto è {prodotto}")

while b == 0:
    b = float(input("inserisci un numero che non sia 0 valido:"))
else:
    divisione = a / b
    print(f"la divisione è {divisione}")

