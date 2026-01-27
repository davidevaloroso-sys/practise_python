''': Scrivi una funzione read_log_file(file_path) che legga il file di log e restituisca una lista di righe.
: Scrivi una funzione parse_log_line(line) che, data una riga di log, estragga e restituisca un dizionario con i seguenti campi:
timestamp
level (es. "error", "warning", "info")
message
rule_id (se presente)'''


def read_log_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        logs = content.split("**")
        # Rimuovi il primo elemento vuoto se presente
        if logs and logs[0].strip() == "":
            logs = logs[1:]
        # Aggiungi "**" all'inizio di ogni log per mantenerlo delimitato
        logs = ["**" + log for log in logs]
    except FileNotFoundError:
        return "file non trovato sul sistema!"
    else:
        return logs


# costruiamo un dizionario K:V che conterrà le analisi di ogni log, con le chiavi seguenti:
#timestamp:data e ora, ruleid:idprocesso, level:warning, message:messaggio del log.
#quindi abbiamo diviso un diz{} con all'interno una lista di diz{} che conterranno ognuno chiave e valore rispetto al log analizato.


def parse_log_line(logs):
    diz = {}
    riga = []
    i=0
    try:
        for log in logs:
            riga.append(log.split("\n"))
                
            rigauno = riga[i][1]
            timestamp = rigauno.split("(")
            
            rigadue = riga[i][2]
            ruleid_level = rigadue.split(" ")
            level = ruleid_level[3].strip("()")
            
            if 0 <= int(level) <= 3:
                level_out = "info"
            elif 4 <= int(level) <= 7:
                level_out = "warning"
            elif int(level) >= 8:
                level_out = "error"

            message = rigadue.split("->") 
            
            diz[i] = {'message': message[1],
                'timestamp': timestamp[0],
                'ruleid': ruleid_level[1],
                'level': level_out,}
            i+=1
    except Exception as e:
        print(e)
    #ritorniamo il dizionario aggiornato con tutti i dizionari per ogni log
    else:
        return diz

'''print(parse_log_line(read_log_file('wazuh_logs.txt')))'''
