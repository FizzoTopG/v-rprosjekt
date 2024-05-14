class spiller():
    def __init__(self, navn: str) -> None:
        self.kamper = 0

    def hent_navn(self):
        navn = self.navn
        return navn

    def hent_antall_kamper(self):
        antall_kamper = self.kamper
        return antall_kamper


    def spill_kamp(self):
        self.kamper += 1
