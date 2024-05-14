kjønn = input("Er du mann eller kvinne? ")
alder = int(input("Hvor gammel er du? "))
status = input("Hva er sivilstatusen din? (singel eller gift) ")
gjeld = int(input("Hvor mye gjeld har du per dags dato? "))
bakgrunnUD = input("Hvilken utdannningsbakgrunn har du? (Ukjent, Grunnskole, Høyskole, Univeristet)")

print(f"Du er en {kjønn} på {alder} år, som er {status} med {gjeld}kr i gjeld. ")

betalinghistorie = []
for i in range(3):
    betalingsstatus = input(f"Betalte du brukeren for {i + 1} måned siden? (betalt/ikke betalt): ")
    betalinghistorie.append(betalingsstatus)

utdanning = {
    "Ukjent":300000,
    "Grunnskole":260000,
    "Høyskole":500000,
    "Universitet":700000
}

ID = int(input("Registrer Kunde-ID: "))
svartlista = [23894, 29741, 10961, 22768, 22803]
if ID in svartlista:
    print("Kan ikke få lån")
else:
    print("Kan få lån")



if betalinghistorie.count() > 1:
    print("Vil ikke betale gjelden sin:(")
elif kjønn == "mann" and utdanning[bakgrunnUD] > gjeld * 3:
    print("Vil betale gjelden sin")
elif kjønn == "mann" and alder < 30 and status == "singel" and gjeld > 100000:
    print("Vil ikke betale gjelden sin :(")
elif kjønn == "mann" and alder < 25 and gjeld > 200000:
    print("Vil ikke betale gjelden sin :(")
elif kjønn == "kvinne" and alder < 28 and gjeld > 300000:
    print("Vil ikke betale gjelden sin :(")
else:
    print("Vil betale gjelden sin:)")

