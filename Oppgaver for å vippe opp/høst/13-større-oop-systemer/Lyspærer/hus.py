from rom import Rom

# Oppgave:
# a) Lag en hus-klasse som inneholder rom
class Hus():
    def __init__(self):
        self._rom: list[Rom] = [] 
        self._strøm = True

# b) Lag en metode legg_til_rom som legger til rom i huset
    def legg_til_rom(self, rom: Rom):
        self._rom.append(rom)

# c) Lag en metode: skru_av_strøm som skrur av alle lys i hele huset
    def sku_av_strøm(self):
        for rom in self._rom:
            rom.skru_av_lys
            
# d) Test huset ditt
if __name__ == "__main__":
    crib = Hus()
    crib.legg_til_rom(Rom())
    