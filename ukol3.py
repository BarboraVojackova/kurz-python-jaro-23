# 1. Import a načtení
import json
with open('body.json', encoding='utf-8') as file:
    points = json.load(file)

prospech = {}

# Stanovené podmínky 60 bodů
for jmeno, body in points.items():
    if body >= 60:
        prospech[jmeno] = 'Pass'
    else:
        prospech[jmeno] = 'Fail'
print(prospech)

# Vyvoření nového JSON souboru
import json
with open ("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(prospech, soubor, ensure_ascii=False)