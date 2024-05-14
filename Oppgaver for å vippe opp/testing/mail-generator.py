# Et program som genererer mailadresser

while True:
    navn = input("Skriv inn hele navnet ditt: ")
    splittet_navn = navn.split()
    antall_navn = len(splittet_navn)
    if antall_navn < 2:
        print("Ugyldig input. Input må bestå av minst to navn") 
    else:
            break

fornavn = splittet_navn[0]
etternavn = splittet_navn[-1]
mail = f"{fornavn.lower()}{etternavn[0].lower()}@viken.no"
print(f"Generelt mailadresse: {mail}") 