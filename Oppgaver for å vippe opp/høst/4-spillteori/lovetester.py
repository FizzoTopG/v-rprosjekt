navn1 = input("Hva heter du? ")
navn2 = input("Hva heter din hemmlige beundrer;) ")
match = 0 

navn1 = navn1.lower()
navn2 = navn2.lower()

forste1 = navn1[0]
forste2 = navn2[0]

lengde1 = len(navn1)
lengde2 = len(navn2)

if lengde1 == lengde2:
    match = 60
elif lengde1 != lengde2 and forste1 == forste2:
    match = 40
else:
    match = 15

sted1 = input("Hvor bor du? ")
sted2 = input("Hvor bor hemmlige beundreren din? ")

sted1 = sted1.lower()
sted2 = sted2.lower()

if sted1 == sted2:
    match = match * 1.5

alder1 = int(input("Hvor gammel er du? "))
alder2 = int(input("Hvor gammel er hemmlige beundreren din? "))

if alder1 < alder2 * 0.5 + 7:
    match = match * 0.5
elif alder1 == alder2:
    match = match * 1.1

if "t" in navn1 or "t" in navn2:
    match = match * 1.02
elif "s" in navn1 and "e" in navn2 and "e" != navn2:
    match = match * 1.15
elif forste1 not in navn2:
    match = match * 0.2

siste_bokstav1 = navn1[-1]
siste_bokstav2 = navn2[-1]

if siste_bokstav1 == forste2:
    match = match + 30
elif siste_bokstav2 == forste1:
    match = match + 30
elif len(navn1) == 0:
    match = 0
elif len(navn2) == 0:
    match = 0


match = round(match)


print(f"Gratulerer dere fikk en {match}% match!")

