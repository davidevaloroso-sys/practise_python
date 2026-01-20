numero = float(input("inserisci un numero e ti dirò se è pari o dispari:"))


if numero %2 == 0:
    print(f"il numero inserito è {numero} ed è pari")
    if numero %5 == 0:
        print(f"il numero {numero} è multiplo di 5")
else:
    print(f"il numero inserito è {numero} ed è dispari")
    if numero %5 == 0:
        print(f"il numero inserito è {numero} ed è multiplo di 5")



