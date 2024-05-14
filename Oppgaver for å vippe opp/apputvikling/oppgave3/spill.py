import os
import platform
import json
from pokemon import Pokemon
from trener import Trener
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

with open("pokemon.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokemoner = data

# Oppretter en liste med pokemon-objekter (objekter av klassen figurer):
figurer = []
for pokemon_ordbok in data:
    ny_figur = Pokemon(pokemon_ordbok)
    figurer.append(ny_figur)


tom_ls = []

 
while True:
    rens_terminal()
    print("-- Pokemon --")  
    print("1: Se pokemonoversikt")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")
    brukervalg = input(">")
    if brukervalg == "1":
        print("-- Pokemonoversikt --")
        for figur in figurer:
            print(figur)
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("-- Treneroversikt --")
        for trener in tom_ls:
            print(trener)
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "3":
        print("Hva heter den nye treneren?")
        navn = input("> ")
        tom_ls.append(Trener(navn))
        
        print("Ny trener er lagt til!")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "4":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig valg")