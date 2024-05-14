elever = [
    {"navn": "Hermine", "hus": "Griffing", "patronus": "Oter"},
    {"navn": "Harry", "hus": "Griffing", "patronus": "Hjort"},
    {"navn": "Ronny", "hus": "Griffing", "patronus": "Jack Russel Terrier"},
    {"navn": "Draco", "hus": "Smygard", "patronus": None}
]

# Oppgave: print dene informasjonen ut i terminalen
# Hermine, griffing, oter

for elev in elever:
    print(elev["navn"],elev["hus"],elev["patronus"] )