'''6) Password (semplice)

Chiedi una password finché non è uguale a "python".

Quando è corretta stampa “Accesso consentito”.

conta i tentativi.'''

password = input("inserisci una password:")

count = 0

while password != "python":
    count += 1
    print("inserisci una password corretta!")
    password = input("inserisci una password:")

print(f"hai tentato di accedere {count} volte")
print("accesso consentito")