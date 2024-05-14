from pokemon import Pokemon

class Trener:
    def __init__(self, navn: str) -> None:
        self.navn: str = navn
        self.pokemonliste: list[Pokemon] = []

    def legg_til(self, pokemon: Pokemon):
        if pokemon not in self.pokemonliste:
            self.pokemonliste.append(pokemon)

    def fjerne_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemonliste:
            self.pokemonliste.remove(pokemon)

    def __str__(self):
        return f"{self.navn} - {len(self.pokemonliste)} pokemon"
    
    def vis_trener(self):
        print(f"-- {self.navn} --")
        for pokemon in self.pokemonliste:
            print(pokemon)
        print()
    def vis_trenere(self):
        print(self.pokemonliste)

    

if __name__ == "__main__":
    print("Tester Trener-klassen")
    testtrener = Trener("fizzo")
    print(testtrener)
