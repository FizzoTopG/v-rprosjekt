elever = ["Hermine", "Harry", "Ronny"]

#Metode 1 uten løkke
print(elever[0])
print(elever[1])
print(elever[2])

#Metode 2 med for-løkker
for elev in elever:
    print(elev)

#Metode 3 - med for-løkke og range
for i in range(len(elever)):
    print(i, elever[i])