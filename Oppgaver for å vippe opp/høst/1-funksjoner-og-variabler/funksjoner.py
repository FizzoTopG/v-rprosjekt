def main():
    person1 = spør_om_navn()
    person2 = spør_om_navn()
    si_hei(person1)
    si_hei(person2)

    print("Hallo, verden")
    si_hei("Fizzo")
    si_hei("Brødre")

def si_hei(til):
    print("Hei", til)

def spør_om_navn():
    return input("Hva heter du?")

main()