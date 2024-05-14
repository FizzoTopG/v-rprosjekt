class Spiller():
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.antall_kamper = 0

    def hent_navn(self):
        return self.navn

    def  hent_kamper(self):
        return self.antall_kamper

    def spill_kamp(self):
        self.antall_kamper += 1

    def sjekk_navn(self, navn: str):
        # returner true hvis spillerens navn inneholder ett av navene
        return navn in self.navn
        # if navn in self.navn:
        #     return True
        # else:
        #     return False
