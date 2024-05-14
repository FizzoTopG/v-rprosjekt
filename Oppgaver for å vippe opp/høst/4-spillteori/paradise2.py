import random

def main():
    print("Velkommen til Troskapstesten")
    spiller1 = 0 
    spiller2 = 0
    for i in range(500):
        resultat = spill(usikker, halvveis)
        spiller1 += resultat[0]
        spiller2 += resultat[1]
        print(spiller1, spiller2)



def snill(beløp):
    # en funksjon for en snill strategi, alltid beholder
    return "behold"

def slem(beløp):
     # en funksjon for en slem strategi, alltid kaster
    return "kast"

def halvveis(beløp):
    if beløp >= 150000:
        return "kast"
    else:
        return "behold"
    
def veldig_usikker(beløp):
    # en spiller som kaster kula 50% av gangene
    tilfeldig_tall = random.randint(1,100)
    if tilfeldig_tall <= 50:
        return "behold"
    else:
        return "kast"
    
def usikker(beløp):
    # en funksjon for en spiller som 30% av gangene kaster kula når beløpet er under 50 000
    # og kaster kula 70% av gangene når beløpet er 50 00 eller mer

    tilfeldig_tall = random.randint(1,100)
    if beløp < 50000:
        if tilfeldig_tall <= 30:
            return "kast"
        else:
            return "behold"
    else:
        if beløp >= 50000:
            if tilfeldig_tall <= 70:
                return "kast"
            else:
                return "behold"
            
def spill(strategi1, strategi2):
    # en funksjon som spiller troskapsteste fra PH
    #funksjonen returnerer en liste med gevinsten til hver spiller
    # f.eks [100 000, 0] eller [150 000, 150 000] eller [0, 80 000] og så videre

    pott = 0 
    for i in range(30):
        pott += 10000 # øker potten med 10 000, 0 i starten
        if strategi1(pott) == "kast":
            return [pott, 0]
        elif strategi2(pott) == "kast":
            return [0,pott]
        
    

    return [pott / 2, pott / 2] # ingen kasta kula, delt pott


main()