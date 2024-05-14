prosent = float(input("Hvor mange prosent fikk du på prøven?"))

if prosent >= 93.33:
    print("Karakter 6")
elif prosent >= 85:
    print("Karakter 5")
elif prosent >= 65:
    print("karakter 4")
elif prosent >= 40:
    print("Karakter 3")
elif prosent >= 20:
    print("karakter 2")
else:
    print("Karakter 1")

# if-setning på en linje
x = 12
y = 14

print("x") if x > y else print("y")

#Samme if-setningen på vanlig måte
if x > y:
    print("x")
else:
    print("y")