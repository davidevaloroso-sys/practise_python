#trovare errori e warning frequenti
#individuare eventi di sicurezza importanti
#assegnare una severità
#creare un report finale 
#Fare delle satistiche opportune


#Critical (Critico): Eventi che indicano un problema grave che potrebbe compromettere il sistema. 
#Error (Errore): Eventi che segnalano un errore significativo che ha impedito un'operazione. 
#Warning (Avviso): Eventi che indicano un problema potenziale, ma non critico. 
#Verbose (Dettagliato): Eventi che forniscono informazioni di traccia dettagliate, spesso usate per il debug.


import json

with open("events.json", "r", encoding="utf-8-sig") as file:
    events = json.load(file)
    #print(events[0])
#dict = {}

#report
with open("report.txt", "r", encoding="utf-8")as rp:
    if rp.read():
        with open("report.txt", "w", encoding="utf-8")as rp:
            rp.write("File Report Resettato, Rielaborazione eventi...")
total = 0
critical = 0
warning = 0
verbose = 0
for data in events:
    total += 1
    for k, v in data.items():
        match v:
            case "Critical":
                critical += 1
                with open("report.txt", "a", encoding="utf-8")as rep:
                    rep.write(str(f"\nReport eventi di tipo Critical:\n{data}"))
            case "Warning":
                warning += 1
                with open("report.txt", "a", encoding="utf-8")as rep:
                    rep.write(str(f"\nReport eventi di tipo Warning:\n {data}"))
            case "Verbose":
                verbose += 1
                with open("report.txt", "a", encoding="utf-8")as rep:
                    rep.write(str(f"\nReport eventi di tipo Verbose :\n{data}"))
with open("report.txt", "a", encoding="utf-8")as repo:
    repo.write(f"\nEventi totali analizzati: {total}\nCritical : {critical}\nWarning : {warning}\nVerbose : {verbose}")
            

#il file events.json è stato volutamente alterato andando a modificare i valori delle chiavi "LevelDisplayName" per controllare il corretto funzionamento del codice.
#ID mapping
#4625 Accesso non riuscito,4720 Creazione di un nuovo utente,4732 Un membro è stato aggiunto a un gruppo locale abilitato alla sicurezza,4672 Privilegi speciali assegnati a un nuovo accesso,1102 Il log di controllo è stato cancellato,4624 Accesso riuscito

