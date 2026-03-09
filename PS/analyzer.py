#trovare errori e warning frequenti
#individuare eventi di sicurezza importanti
#assegnare una severità
#creare un report finale 
#Fare delle satistiche opportune

import json

with open("events.json", "r", encoding="utf-8-sig") as file:
    events = json.load(file)






eventi = [
    {
        "Id": e.get("Id"),
        "Message": e.get("Message"),
        "LogName": e.get("LogName"),
        "Level": e.get("Level"),
        "LevelDisplayName": e.get("LevelDisplayName"),
        "TimeCreated": e.get("TimeCreated"),
        "TaskDisplayName": e.get("TaskDisplayName"),
        "KeywordsDisplayNames": e.get("KeywordsDisplayNames"),
        "MachineName": e.get("MachineName"),
    }
    for e in events
]
print(eventi)