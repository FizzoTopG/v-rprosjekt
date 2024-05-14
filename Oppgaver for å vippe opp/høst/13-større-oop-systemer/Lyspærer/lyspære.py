# Lyspære
class Lyspære():
    def __init__(self):
        self._på = False #_på er at det er en "privat" metode og får å kunne endre på verdien må vi bruke metoder

    def tenn(self):
        self._på = True

    def slukk(self):
        self._på = False

    def er_på(self):
        #returnerer true hvis pæra er på og false hvis pæra er av
        return self._på


#Linja under sørger for at test koden kunn kjøres når vi trykker play på DENNE fila
if __name__ == "__main__":
    # Test kode
    min_pære = Lyspære()
    stue_pære = Lyspære()
    soverom_pære = Lyspære()

    stue_pære.tenn()

    if stue_pære.er_på():
        print("Pæra i stua er på!")

    # Slutt på test kode