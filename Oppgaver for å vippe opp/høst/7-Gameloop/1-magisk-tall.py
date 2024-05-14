import random

# Gameloop-mønsteret

# 1. Oppsett
magisk_tall = random.randint(1,10)
antall_forsøk = 0
# Gameloop:4
while True:
    # 2. Håndter input
    brukerinput = int(input("Hva er det magiske tallet? "))
    if brukerinput == "avslutt":
        break
    tall = int(brukerinput)
    # 3. Oppdater spill
    antall_forsøk += 1
    # 4. Tegn (print)
    if brukerinput > magisk_tall:
        print("For høyt")
    elif brukerinput < brukerinput:
        print("For lavt")
    else:
        print(f"Riktig antall forsøk: {antall_forsøk}")
        break