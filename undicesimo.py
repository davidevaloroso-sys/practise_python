'''11) Conta lettere

Leggi una parola e conta quante volte compare la lettera 'a'.
rendilo case-insensitive (trasforma in minuscolo prima).'''


parola = input("inserisci una parola e conterò quante volte 'a' è presente:")

parola = parola.lower()
count = 0
for c in parola:
    if c == "a":
        count += 1

print(f"la letta 'a' compare: {count} volte")