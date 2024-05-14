# Et program som fortsetter helt til bruker har skrevet riktig input

år = 2024                                                # Oppretter variabel år som får verdien 2024

while True:                                              # Lager en evig løkke, while True
    try:                                                 # Prøver koden
        alder = int(input("Hvor gammel blir du i år? ")) # Oppretter variabelen alder som finner alder til spiller ved hjelp av input
        break                                            # bryter den evige løkken hvis spiller har skrevet inn riktig input
    except:                                              # Hvis try ikke funker eller er ugyldig , prøv dette
        print("Ugyldig input. Input må være et tall")    # Printer en fin feilmelding

fødselsår = år - alder                                   # Oppretter variabelen fødselsår å gi den verdien til år minus alder
print(f"Du er født i {fødselsår}")                       # Printer ut fødselsåret til spiller på en fin måte