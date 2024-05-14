# Et program som finner fødselsår basert på alder

år = 2024
try:
    alder = int(input("Hvor gammel blir du iår?: "))
    fødselsår = år - alder
    print(f"Du er født i {fødselsår}")
except:
    print("Ugyldig input. Input må være et tall")

print("Koden fortsetter...")

# Et annet eksempel
try:
    tall = int(input("SKriv et tall: "))
except:
    print("Ugyldig input. Setter 'tall' til 10")
    tall = 10

print(tall) # tall er 10 hvis brukeren ikke skriver inn et tall i input