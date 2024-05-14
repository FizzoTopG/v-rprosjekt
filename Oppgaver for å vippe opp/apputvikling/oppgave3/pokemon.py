class Pokemon:
    def __init__(self, pokemon_ordbok: dict,) -> None:
        self.id = int = pokemon_ordbok["id"]
        self.navn = str = pokemon_ordbok["name"]["english"]
        self.type = list = pokemon_ordbok["type"]
        self.hp = int = pokemon_ordbok["base"]["HP"]
        self.attack = int = pokemon_ordbok["base"]["Attack"]
        self.defence = int = pokemon_ordbok["base"]["Defense"]
        self.spattack = int = pokemon_ordbok["base"]["Sp. Attack"]
        self.spdefence = int = pokemon_ordbok["base"]["Sp. Defense"]
        self.speed = int = pokemon_ordbok["base"]["Speed"]

    def __str__(self):
        # en spesiell metode som bestemmer hvordan en poltiker skal printes ut
        return f"{self.navn} (Speed: {self.speed})"
    

if __name__ == "__main__":
    print("Tester pokemon-klassen")