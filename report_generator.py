
#tutte le funzioni necessarie per il generator del report
def filter_by_level(diz, level):
    target_level = []
    if  level.lower() not in ["info", "warning", "error"]:
        return None
    a = False
    for i in diz:
        if diz[i]['level'] == level:
            a = True
            target_level.append(i)
            print(diz[i])
    if a is False:
        print(f"nessun log trovato per {level}")

#ritorna none se non viene utilizzato il livello giusto come valore, altrimenti printa il log corretto.
#logs = read_log_file('wazuh_logs.txt')
#print(parse_log_line(logs))
        

#filter_by_level(parse_log_line(logs), 'error')

def count_events_by_level(diz):
    event_count = {'info': 0 , 'warning': 0 , 'error': 0 }
    for i in diz:
        level = diz[i]['level']
        event_count[level] += 1
            
    return event_count

#print(count_events_by_level(parse_log_line(logs)))


'''Scrivi una funzione generate_report(logs, output_file) che generi un file di testo con:
Il numero totale di eventi
Il conteggio degli eventi per livello
I primi 5 eventi con livello "error" (se presenti)'''


def generate_report(diz, output_file):
    tot_eventi = len(diz)
    counts = count_events_by_level(diz)
    
    # Filtra gli errori
    errori = []
    for i in diz:
        if diz[i]['level'] == 'error':
            errori.append(diz[i])
    
    # Prendi i primi 5 errori
    errori_top5 = errori[:5]
    
    with open(output_file, 'w') as file:
        file.write("Report of log events:\n")
        file.write(f"Totale eventi: {tot_eventi}\n")
        file.write(f"Info: {count_events_by_level(diz)}\n")
        
        file.write("Primi 5 errori:\n")
        for idx, errore in enumerate(errori_top5, 1):
            timestamp = errore['timestamp']
            ruleid = errore['ruleid']
            message = errore['message'].strip()
            file.write(f"{idx}. [{timestamp}] Rule {ruleid} - {message}\n")

#print(generate_report(parse_log_line(logs), 'output_log.txt'))

