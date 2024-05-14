fil = open("input.txt")
data = fil.read()
linjer = data.split("\n") # opt+shift+7 ->

sum = 0

for linje in linjer:
    tall = []
    for bokstav in linje:
        if bokstav.isdigit():
            tall.append(bokstav)
    først_og_sist = tall[0] + tall[-1]
    sum += int(først_og_sist)

print(sum)

    