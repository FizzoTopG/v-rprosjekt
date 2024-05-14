def main():
    antall = hent_nummer()
    print_mjau(antall)

def hent_nummer():
    while True:
        antall = int(input("Skriv et positivt tall"))
        if antall > 0:
            break
        print("Ugyldig tall")

def print_mjau(antall): 
    print("Mjau\n" * antall, end="")

main()