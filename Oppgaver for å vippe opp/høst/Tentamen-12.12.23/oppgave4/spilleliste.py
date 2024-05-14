from sang import Sang

class Spilleliste():
    def __init__(self, navn: str, sanger: list) -> None:
        self.navn = navn
        self.sanger = sanger
        sanger = []
        
    def legg_til_sang(self, Sang):
        self.sanger.append(Sang)
    #   return self.sanger

# Fizzolist = Spilleliste("Fizzo", [])
# print(Fizzolist.legg_til_sang(Sang("STARGAZING", "Travis Scott"))) # funker


    def lengde(self):
        return len(self.sanger)

# Fizzolist = Spilleliste("Fizzo", [])
# Fizzolist.legg_til_sang(Sang("STARGAZING", "Travis Scott"))
# Fizzolist.legg_til_sang(Sang("GODS PLAN", "Drake"))
# print(Fizzolist.lengde()) # 2 printes pga linjene over (bare for å demonstrere)


    # def spill_alle(self):
     
# Fizzolist = Spilleliste("Fizzo", ["STARGAZING", "GODS PLAN"])
# print(Fizzolist.spill_alle())


    def tittel_i_liste(self, tittel:str):
        if tittel in self.sanger:
            return True
        else:
            return False
        
# Fizzolist = Spilleliste("Fizzo", ["STARGAZING", "GODS PLAN"])
# print(Fizzolist.tittel_i_liste("GODS PLAN")) # True
# print(Fizzolist.tittel_i_liste("Bad blood")) # False


    # def artistsliste(self, artist:str):
    #     ny_list = []
    #     for sang in self.sanger:
    #         if sang == artist:
    #             ny_list.append(artist)
    #     return ny_list

    def artistsliste(self, artist:str):
        ny_list = []
        for sang in self.sanger:
            if artist == sang.artist:
                ny_list.append(sang)
        return ny_list
    
# Fizzolist = Spilleliste("Fizzo", [])
# Fizzolist.legg_til_sang(Sang("STARGAZING", "Travis Scott"))
# Fizzolist.legg_til_sang(Sang("GODS PLAN", "Drake"))
# Fizzolist.legg_til_sang(Sang("Bad blood", "Taylor Swift"))
# Fizzolist.legg_til_sang(Sang("Nonstop", "Drake"))
# Fizzolist.legg_til_sang(Sang("I´m upset", "Drake"))

# print(Fizzolist.artistsliste("Drake")) # får en liste med alle Drake sangene i Fizzolist
            


