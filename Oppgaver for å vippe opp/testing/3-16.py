print("Skriv in poengsummen din")
Poengsum = int(input("> "))
if Poengsum < 50:
    print("Ikke bestått")
elif Poengsum > 50 and Poengsum < 69:
    print("bestått")
elif Poengsum > 70 and Poengsum < 89:
    print("Godt bestått")
elif Poengsum > 90 and Poengsum < 100:
    print("Mykje godt bestått")
else:
    print("ikke gyldig poengsum")
