class Spiller():
    def __init__(self, navn: str, antall_kamper: int) -> None:
        self.navn = navn
        antall_kamper = 0

    def hent_navn(self):
        return self.navn
    
    def hent_antall_kamper(self):
        return self.antall_kamper
    
    def spill_kamp(self):
        self.antall_kamp += 1

    def sjekk_navn(self, navn: str):
        if navn in self.navn:
            return True
        else:
            return False

fm = Spiller("Faizan Rasul Mirza", 0)

print(fm.sjekk_navn("Razul"))



        