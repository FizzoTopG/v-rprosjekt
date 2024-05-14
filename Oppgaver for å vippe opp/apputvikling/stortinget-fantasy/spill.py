import os 
import sys
import json
from politiker import Politiker
from fantasiparti import Fantasiparti

def rens_terminal():
#   if sys.platform == "Windows": # gammel
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

# 1. Oppsett
#åpner json fila og putter alt innholdet i variabelen data
with open("representanter.json", "r", encoding="utf-8",) as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"] #henter ut lista med representanter

# Oppretter en liste med politiker-objekter (objekter av klassen politiker):
politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)

print("-- Velkommen til stortinget fantasy --")

print()
print("Du må stifte et parti for å spille")
print("Hva skal partiet ditt hete?")
partinavn = input("> ")
print("Hva heter du?")
spillernavn = input("> ")
spillerparti = Fantasiparti(partinavn, spillernavn)
print(f"Gratulerer! Det nye partiet {partinavn} ble stiftet med partilederen {spillernavn}")
input("Trykk enter for å starte spillet")

while True:
    rens_terminal()
    print(" -- Stortinget-fantasy -- ")

    print("1: Vis politikeroversikt")  
    print("2: Mitt parti")
    print("3: Avslutt")
    brukervalg = input("> ")

    if brukervalg == "1":
        print("politikeroversikt")
        for politiker in politikere:
            print(politiker)
        input("Trykk enter for å gå tilbake til hoved menyen")
    elif brukervalg == "2":
        print("Mitt parti")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "3":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("ugyldig input")
        input("Trykk enter for å gå tilbake til hovedmeny")


