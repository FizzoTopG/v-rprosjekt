class Person():
    def __init__(self, fornavn, etternavn, fødselår) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselår = fødselår
        self.familie = []


    def beregnAlder(self):
        return 2023 - self.fødselår
    
    def vis_info(self):
        print(self.fornavn, self.etternavn, self.beregnAlder())

    def legg_til_familiemedlem(self, person):
        self.familie.append(person)

    def vis_familie_info(self):
        for medlem in self.familie:
            medlem.vis_info()
        
fm = Person("Faian", "Mirza", 2005)
fm.vis_info()

ab = Person("Elias", "Abdeladim", 2005)

ab.legg_til_familiemedlem(ab)

print(ab.vis_familie_info())





