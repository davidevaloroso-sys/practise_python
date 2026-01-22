#!/bin/bash
#
# Scopo:
#   Dato un file di log (es. vsftpd/ftp) e una fascia oraria + data,
#   conta i tentativi di "FAIL LOGIN" raggruppandoli per IP.
#
# Uso:
#   ./script.sh HH_INI HH_END YYYY-MM-DD /path/logFtp.log
#
# Esempio:
#   ./script.sh 14 18 2026-01-19 /var/log/vsftpd.log
#
# Output:
#   IP -> numero di tentativi falliti nella fascia oraria e data richieste


########################################
# 1) Ri*levamento sistema operativo
########################################
# Nota: questa parte non è strettamente necessaria per lo script (non usi comandi
# differenti a seconda dell'OS), ma la mantengo perché l'avevi e può servire
# come "guardrail" per ambienti non previsti.

if [ -f /etc/os-release ]; then
    OS_ID=$(grep "^ID=" /etc/os-release | cut -d= -f2 | tr -d '"')
else
    echo "Impossibile determinare il sistema operativo (manca /etc/os-release)." >&2
    exit 1
fi

case "$OS_ID" in
    ubuntu|debian)
        echo "Sistema rilevato: Ubuntu/Debian"
        ;;
    rhel|centos|fedora)
        echo "Sistema rilevato: Red Hat-like"
        ;;
    *)
        echo "Sistema operativo non supportato: $OS_ID" >&2
        exit 1
        ;;
esac

echo

########################################
# 2) Controllo parametri
########################################
if [ "$#" -ne 4 ]; then
    echo "Uso: $0 HH_INI HH_END YYYY-MM-DD /path/logFtp.log" >&2
    exit 1
fi

HOUR_START="$1"   # formato atteso: "00".."23" o anche "0".."23"? qui imponiamo 2 cifre
HOUR_END="$2"
DATE_PARAM="$3"   # formato atteso: YYYY-MM-DD
LOG_FILE="$4"

########################################
# 3) Controllo file di log
########################################
if [ ! -f "$LOG_FILE" ]; then
    echo "File di log non trovato: $LOG_FILE" >&2
    exit 1
fi

if [ ! -r "$LOG_FILE" ]; then
    echo "File di log non leggibile: $LOG_FILE (usa sudo o cambia i permessi)" >&2
    exit 1
fi

########################################
# 4) Controlli su formato e range ore
########################################
# Richiediamo esattamente due cifre per coerenza con l'uso che ne facciamo dopo.
# (Se vuoi accettare anche "9" al posto di "09", te lo modifico facilmente.)
if ! [[ "$HOUR_START" =~ ^[0-9]{2}$ ]] || ! [[ "$HOUR_END" =~ ^[0-9]{2}$ ]]; then
    echo "Le ore devono essere nel formato HH (00-23), es: 09 18" >&2
    exit 1
fi

# Range 00-23
if [ "$HOUR_START" -lt 0 ] || [ "$HOUR_START" -gt 23 ] || \
   [ "$HOUR_END"   -lt 0 ] || [ "$HOUR_END"   -gt 23 ]; then
    echo "Le ore devono essere comprese tra 00 e 23" >&2
    exit 1
fi

# Ordine (inizio <= fine)
if [ "$HOUR_START" -gt "$HOUR_END" ]; then
    echo "L'ora iniziale deve essere <= ora finale" >&2
    exit 1
fi

########################################
# 5) Parsing e validazione data YYYY-MM-DD
########################################
# Prima controlliamo il formato base con una regex.
if ! [[ "$DATE_PARAM" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "Formato data non valido. Atteso YYYY-MM-DD, es: 2026-01-19" >&2
    exit 1
fi

YEAR="${DATE_PARAM:0:4}"
MONTH_NUM="${DATE_PARAM:5:2}"
DAY="${DATE_PARAM:8:2}"

# Convertiamo mese numerico in abbreviazione inglese (formato tipico dei log)
case "$MONTH_NUM" in
  "01") LOG_MONTH="Jan" ;;
  "02") LOG_MONTH="Feb" ;;
  "03") LOG_MONTH="Mar" ;;
  "04") LOG_MONTH="Apr" ;;
  "05") LOG_MONTH="May" ;;
  "06") LOG_MONTH="Jun" ;;
  "07") LOG_MONTH="Jul" ;;
  "08") LOG_MONTH="Aug" ;;
  "09") LOG_MONTH="Sep" ;;
  "10") LOG_MONTH="Oct" ;;
  "11") LOG_MONTH="Nov" ;;
  "12") LOG_MONTH="Dec" ;;
  *)
    echo "Mese non valido in DATA: $DATE_PARAM" >&2
    exit 1
    ;;
esac

# IMPORTANTISSIMO:
# In bash, in aritmetica, numeri con zero iniziale (08, 09) possono creare problemi.
# Per evitarlo, quando trasformiamo stringhe numeriche in numeri usiamo sempre 10#...
HOUR_START_DEC=$((10#$HOUR_START))
HOUR_END_DEC=$((10#$HOUR_END))
DAY_DEC=$((10#$DAY))

echo "Analisi falliti dal log: $LOG_FILE"
echo "Fascia oraria: $HOUR_START - $HOUR_END"
echo "Data richiesta: $DATE_PARAM"
echo

########################################
# 6) Mappa IP -> conteggio
########################################
# Associative array: IP_COUNTS["1.2.3.4"]=N
declare -A IP_COUNTS

########################################
# 7) Lettura del log e conteggio
########################################
# Approccio robusto:
# - prima filtro "FAIL LOGIN:" (così scarto presto la maggior parte delle righe)
# - poi parse dei campi: Mon Jan 19 14:52:04 2026 ...
# - confronto mese/giorno/anno
# - estrazione ora e confronto in decimale
# - estrazione IP tramite regex sul pattern Client "::ffff:IP"
#
# Perché non facciamo: if [[ line == "Jan 19 2026" ]] ?
# Perché nel log la sequenza è "Jan 19 14:52:04 2026", quindi "Jan 19 2026"
# NON compare mai come sottostringa contigua.

while IFS= read -r line; do
    # 1) deve essere un fallimento di login (la riga CONTIENE "FAIL LOGIN:")
    [[ "$line" == *"FAIL LOGIN:"* ]] || continue

    # 2) estraggo i primi campi del log:
    #    Mon Jan 19 14:52:04 2026 ...
    read -r _ mon day time_f year _ <<< "$line" || continue

    # 3) filtro data (mese/giorno/anno)
    [[ "$mon" == "$LOG_MONTH" ]] || continue
    (( 10#$day == DAY_DEC )) || continue
    [[ "$year" == "$YEAR" ]] || continue

    # 4) filtro fascia oraria
    hour_dec=$((10#${time_f:0:2}))
    (( hour_dec < HOUR_START_DEC || hour_dec > HOUR_END_DEC )) && continue

    # 5) estrazione IP
    # Supporta: Client "::ffff:192.168.1.14" e Client "192.168.1.14"
    if [[ "$line" =~ Client\ \"(::ffff:)?([0-9]{1,3}(\.[0-9]{1,3}){3})\" ]]; then
        ip="${BASH_REMATCH[2]}"
        IP_COUNTS["$ip"]=$(( ${IP_COUNTS["$ip"]:-0} + 1 ))
    fi

done < "$LOG_FILE"


########################################
# 8) Output
########################################

echo "Risultato (IP - numero di tentativi di login falliti):"
if [ "${#IP_COUNTS[@]}" -eq 0 ]; then
    echo "Nessun tentativo di login fallito trovato nella fascia indicata."
else
    # Stampa non ordinata (ordine hash).
    # Se vuoi ordinare per conteggio decrescente te lo faccio in 2 righe con sort.
    for ip in "${!IP_COUNTS[@]}"; do
        echo "$ip ${IP_COUNTS[$ip]} volte"
    done
fi
