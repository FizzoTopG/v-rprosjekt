class Person():
    def __init__(self, fornavn, etternavn, fødselsår: int) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

    def beregn_alder(self):
        return 2023 - self.fødselsår
    
    def vis_info(self):
        print(self.fornavn, self.etternavn, self.beregn_alder())


fizzo = Person("Faizan", "Mirza", 2005)

print(fizzo.vis_info())