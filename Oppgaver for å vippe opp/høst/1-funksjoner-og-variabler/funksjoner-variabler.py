# Innebygde funksjoner
print("Hei på deg!") # en innebgyd funksjon som printer "Hei på deg" i terminalen
input("Hva heter du??") # en innebygd som printer argumenter (hva heter du??), lar brukerern
# skrive inn noe og returnere det til brukeren som skriver inn

# Argumenter
print("Hei på deg!") # Funkjsoner kan ta i mot argumenter, de skrives mellom parantesene
print("hallo, ", "Thor") # noen funksjoner kan ta i mot flere argumenter, da skiller vi
# argumentene med komma

print("Hei,", end=" ", sep=" ") # end og sep i dette tilfellet navngitt argument (named argument)
print("Verden")


# Metoder
## Metoder er funksjoner som hører til "ting", eksempel metoder sommhører til strings
navn = "Thor Christian Coward"
fornavn, mellomnavn, etternavn = navn.split() # split er en metode som splitter en stringpå argumentet


#strings
##Strings skrives mellom anførselstegn, enten enkle ' ' eller doble " "

# Egne funksjoner

def si_hei(til): # definerer en egen funksjon med navn si_hei som tar inn en parameter med navn til
    print("Hei", til)

def spør_om_navn(): # returerer stringen som kommer, tar ikke inn parameter
    return input("Hva heter du?")

# parameter vs. argument