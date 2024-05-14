# oppgave: Lag et program som spør brukeren: "hva 
# er x og hva er y?" og lagre veridene i to
# variabler x og y 
x = int(input("Hva er x "))
y = int(input("Hva er y "))

if x > y:
    print("X er større enn y")
if x >= y:
    print("x er større eller lik y")
if x == y:
    print("x er lik y")

print( "Ferdig")