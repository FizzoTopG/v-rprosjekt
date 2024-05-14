# input er en funksjon som tar inn et argument og returnerer det brukern skriver inn
navn = input("Hva heter du? (Fornavn og etternavn)")

# Hva er navn??? En variabel som inneholder en string
fornavn, etternavn = navn.split(" ") # splitter opp navn (en string tekst)
fornavn = fornavn.capitalize()
navn = navn.title()

#Print hallo, NAVN i terminalen
print("Hallo,", fornavn)
print("Ditt fulle navn er:", navn)