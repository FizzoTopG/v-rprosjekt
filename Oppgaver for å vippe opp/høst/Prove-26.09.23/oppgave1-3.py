from random import randint

kast = int(input("Hvor mange ganger vil du kaste terningen? (tall): "))

terningkast = randint(1,6)

antallkast = []

def kast_terninger(kast):
    for i in kast:
        print(terningkast + i)

    return antallkast

#fikk det ikke helt til, prøvde meg frem hvertfall