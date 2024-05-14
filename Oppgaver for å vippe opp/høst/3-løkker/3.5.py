liste = [6, -4, 7, -2, 8, -3, 9, -11]
minst = liste[0]
max = liste[0]

for i in liste:
    if i < minst:
        minst = i

for i in liste:
    if i > max:
        max = i

print(minst)
print(max)