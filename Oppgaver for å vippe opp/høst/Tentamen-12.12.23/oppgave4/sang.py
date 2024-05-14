class Sang():
    def __init__(self, tittel:str, artist:str) -> None:
        self.tittel = tittel
        self.artist = artist
        self.avspillinger = 0

    def spill(self):
        self.avspillinger += 1
        return print("STARGAZING - Travis Scott")
    

# STARGAZING = Sang("STARGAZING","Travis Scott")
# print(STARGAZING.spill())

    def sjekk_tittel(self, tittel:str):
        if self.tittel == tittel:
            return True
        else:
            return False

# STARGAZING = Sang("STARGAZING","Travis Scott")
# print(STARGAZING.sjekk_tittel("STARGAZING")) # True
# print(STARGAZING.sjekk_tittel("Seint i går")) # False

    def sjekk_artist(self, artist:str):
        if self.artist == artist:
            return True
        else:
            return False

# STARGAZING = Sang("STARGAZING","Travis Scott")
# print(STARGAZING.sjekk_artist("Travis Scott")) # True
# print(STARGAZING.sjekk_artist("Drake")) # False

    def __repr__(self) -> str:
        str = f'{self.artist} - {self.tittel}'
        return str
