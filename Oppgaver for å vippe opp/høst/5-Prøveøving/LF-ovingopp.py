Oppgave 1 og 2

print("Hva er din sivilstatus?")
sivilstatus = input("gift/ugift: ")
print("Hvilket kjønn er du?")
kjonn = input("mann/kvinne: ")
print("Hvor gammel er du?")
alder = int(input("alder: "))
print("Hvor mye gjeld har du?")
gjeld = int(input("kr: "))
print(f'Du er en {sivilstatus} {kjonn} på {alder} år med {gjeld} kr i gjeld')
    
if kjonn == "mann" and alder < 30 and gjeld > 100000 and sivilstatus == "singel":
    print("vil ikke betale")
elif alder < 25 and gjeld > 200000:
    print("vil ikke betale")
elif kjonn == "kvinne" and alder < 28 and gjeld > 300000 and sivilstatus == "singel":
    print("vil ikke betale")
else:
    print("vil betale")


Oppgave 3

print("Hva er din sivilstatus?")
sivilstatus = input("gift/ugift: ")
print("Hvilket kjønn er du?")
kjonn = input("mann/kvinne: ")
print("Hvor gammel er du?")
alder = int(input("alder: "))
print("Hvor mye gjeld har du?")
gjeld = int(input("kr: "))

print(f'Du er en {sivilstatus} {kjonn} på {alder} år med {gjeld} kr i gjeld')

betalingshistorikk = []
for i in range(3):
    betalingsstatus = input(f'Betalte brukeren for {i + 1} måneder siden? (betalt/ikke_betalt): ')
    betalingshistorikk.append(betalingsstatus)

if betalingshistorikk.count("ikke_betalt") > 1:
    print("vil ikke betale")
elif kjonn == "mann" and alder < 30 and gjeld > 100000 and sivilstatus == "singel":
    print("vil ikke betale")
elif alder < 25 and gjeld > 200000:
    print("vil ikke betale")
elif kjonn == "kvinne" and alder < 28 and gjeld > 300000 and sivilstatus == "singel":
    print("vil ikke betale")
else:
    print("vil betale")

Oppgave 4

utdanning = {
        "ukjent" : 300000,
        "grunnskole" : 260000,
        "høyskole" : 500000,
        "universitet" : 700000,
}

print("Hva er din sivilstatus?")
sivilstatus = input("gift/ugift: ")
print("Hvilket kjønn er du?")
kjonn = input("mann/kvinne: ")
print("Hvor gammel er du?")
alder = int(input("alder: "))
print("Hvor mye gjeld har du?")
gjeld = int(input("kr: "))
print("Hva er din høyeste fullførte utdanning?")
utdanningsnivå = input("(ukjent/grunnskole/høyskole/universitet): ")

print(f'Du er en {sivilstatus} {kjonn} på {alder} år med {gjeld} kr i gjeld')
betalingshistorikk = []
for i in range(3):
    betalingsstatus = input(f'Betalte brukeren for {i + 1} måneder siden? (betalt/ikke_betalt): ')
    betalingshistorikk.append(betalingsstatus)

if betalingshistorikk.count("ikke_betalt") > 1:
    print("vil ikke betale")
elif kjonn == "mann" and utdanning[utdanningsnivå] > gjeld * 3:
    print("vil ikke betale")
elif sivilstatus == "singel" and kjonn == "mann" and alder < 30 and gjeld > 100000:
    print("vil ikke betale")
elif kjonn == "mann" and alder < 25 and gjeld > 200000:
    print("vil ikke betale")
elif kjonn == "kvinne" and sivilstatus == "singel" and alder < 28 and gjeld > 300000:
    print("vil ikke betale")
else:
    print("vil betale")


Oppgave 5


svartelisten = [23894, 29741, 10961, 22768, 22803]
print("Hva er din ID?")
id = int(input("ID: "))
if id in svartelisten:
    print("vil ikke betale")
else:
    print("vil betale")

