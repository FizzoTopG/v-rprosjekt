kjønn = input("Er du mann eller kvinne? ")
alder = int(input("Hvor gammel er du? "))
status = input("Hva er sivilstatusen din? (singel eller gift) ")
gjeld = int(input("Hvor mye gjeld har du per dags dato? "))

print(f"Du er en {kjønn} på {alder} år, som er {status} med {gjeld}kr i gjeld. ")

if kjønn == "mann" and alder < 30 and status == "singel" and gjeld > 100000:
    print("Vil ikke betale gjelden sin :(")
elif kjønn == "mann" and alder < 25 and gjeld > 200000:
    print("Vil ikke betale gjelden sin :(")
elif kjønn == "kvinne" and alder < 28 and gjeld > 300000:
    print("Vil ikke betale gjelden sin :(")
else:
    print("Vil betale gjelden sin:)")