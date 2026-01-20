'''8) Indovina il numero (senza random)

Fissa un numero segreto nel codice (es. 37).

L’utente prova: il programma dice “troppo alto/basso”.

stampa i tentativi e ferma dopo 10 tentativi (se fallisce: “Hai perso”).'''


secret = 37

num = int(input("inserisci un intero e prova ad indovinare il numero segreto!"))
counthigh = 0
countmin = 0
while num > secret:
    counthigh += 1
    print("il numero è più alto! Riprova:")
    num = int(input("inserisci un intero e prova ad indovinare il numero segreto!"))
while num < secret:
    countmin += 1
    print("il numero è più basso! Riprova:")
    num = int(input("inserisci un intero e prova ad indovinare il numero segreto!"))

if num == secret:
    print("hai trovato il numero segreto!")
print(counthigh + countmin)