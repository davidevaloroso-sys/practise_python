from log_parser import read_log_file as leggi_file_log, parse_log_line as analizza_riga
from report_generator import filter_by_level as filtra_per_livello, count_events_by_level as conta_eventi_per_livello, generate_report as genera_report



'''Crea uno script main.py che importi i moduli sopra e:
Legga il file di log (passato come argomento da riga di comando)
Chiami le funzioni per il parsing, il filtraggio e la generazione del report
Stampi a video un riassunto del report'''


file = input("inserisci il nome del file da analizzare: ")

file_letto = leggi_file_log(file)

diz_log = analizza_riga(file_letto)

livello = input("inserisci il livello che vuoi analizzare: ")

livello_filtrato = filtra_per_livello(diz_log, livello)

nome_report = input("inserisci il nome del file di output: ")

report = genera_report(diz_log, nome_report)


with open(nome_report, "r") as f:
    contenuto = f.read()
    print(contenuto)


####################################################
# code made by Valoroso Davide & Francesco D'amelio.
####################################################



