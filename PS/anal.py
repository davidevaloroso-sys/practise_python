import json
import re
from collections import Counter
import csv
from datetime import datetime

def parse_multi_json(file_path):
    """Parsa file JSON multipli da PowerShell Get-WinEvent"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Trova tutti gli array JSON validi
    json_arrays = re.findall(r'\[\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}\s*\]', content, re.DOTALL)
    all_events = []
    
    for json_str in json_arrays:
        try:
            data = json.loads(json_str)
            if isinstance(data, list):
                all_events.extend(data)
        except json.JSONDecodeError:
            continue
    
    return all_events

# CARICA E PULISCI DATI
events = parse_multi_json("events.json")
eventi = [
    {
        "Id": e.get("Id"),
        "Message": str(e.get("Message", ""))[:200] + "..." if len(str(e.get("Message", ""))) > 200 else str(e.get("Message", "")),
        "LogName": e.get("LogName"),
        "Level": e.get("Level"),
        "LevelDisplayName": e.get("LevelDisplayName"),
        "TimeCreated": e.get("TimeCreated"),
        "TaskDisplayName": e.get("TaskDisplayName"),
        "KeywordsDisplayNames": e.get("KeywordsDisplayNames", []),
        "MachineName": e.get("MachineName"),
    }
    for e in events
]

print(f" ANALISI EVENTI WINDOWS - {len(eventi)} totali")

# 1️ ERRORI E WARNING FREQUENTI
print("\n ERRORI E WARNING (Top 10 per ID)")
critical_levels = ["Error", "Warning", "Critical", "Errore"]
errors = [e for e in eventi if e["LevelDisplayName"] in critical_levels]
error_ids = Counter(e["Id"] for e in errors)
for id_, count in error_ids.most_common(10):
    print(f"  ID {id_}: {count} volte")

# 2️ EVENTI SICUREZZA IMPORTANTI
print("\n EVENTI SECURITY CRITICI")
security_critical_ids = {4625: "Logon fallito", 4624: "Logon riuscito", 
                        4720: "Utente creato", 4732: "Utente modificato", 
                        4672: "Privilegi assegnati", 4673: "Privilegi usati",
                        1102: "Audit log cancellato", 4616: "Log sicurezza avviato"}
security_events = [e for e in eventi if e["LogName"] == "Security" and e["Id"] in security_critical_ids]
print(f"Trovati {len(security_events)} eventi critici")
for e in security_events[-5:]:  # Ultimi 5
    desc = security_critical_ids.get(e["Id"], "Altro")
    print(f"  ID:{e['Id']} ({desc}) - {e['TaskDisplayName']}")

# 3️ ASSEGNAZIONE SEVERITÀ
def get_severity(e):
    if e.get("LevelDisplayName") in ("Error", "Critical", "Errore"):
        return "HIGH"
    if e.get("LevelDisplayName") == "Warning":
        return "MEDIUM"
    if e.get("LogName") == "Security" and e["Id"] in security_critical_ids:
        return "SECURITY"
    return "LOW"

severities = Counter(get_severity(e) for e in eventi)
print("\n DISTRIBUZIONE SEVERITÀ")
for sev, count in severities.most_common():
    perc = (count/len(eventi))*100
    print(f"  {sev}: {count} ({perc:.1f}%)")

# 4️ STATISTICHE
print("\n STATISTICHE PRINCIPALI")
logs = Counter(e["LogName"] for e in eventi)
for log, count in logs.most_common():
    print(f"  {log}: {count}")
top_tasks = Counter(e["TaskDisplayName"] for e in eventi if e["TaskDisplayName"])
print(f"  Top Task: {top_tasks.most_common(3)}")

# 5️ REPORT CSV (solo critici)
print("\n Salvataggio report...")
with open("report_critici.csv", "w", newline="", encoding="utf-8-sig") as f:
    fieldnames = ["Id", "LogName", "LevelDisplayName", "TaskDisplayName", "Message", "TimeCreated"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    critici = [e for e in eventi if get_severity(e) in ("HIGH", " MEDIUM", "SECURITY")]
    writer.writerows(critici)

print(" ANALISI COMPLETATA!")
print(" Report: report_critici.csv")
