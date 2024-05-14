from lyspære import Lyspære

class Rom:
    def __init__(self) -> None:
        self._pærer: list[Lyspære] = []

    def legg_til_pære(self, pære):
        self._pærer.append(pære)

    def skru_på_lys(self):
        for pære in self._pærer:
            pære.tenn()

    def skru_av_lys(self):
        for pære in self._pærer:
            pære.slukk()

    def skru_på_lys_n(self, n: int):
        self._pære[n].slukk()

    def __str__(self):
        return f"Rom ({len(self._pære)} pærer)"

if __name__ == "__main__":
    print("Tester rom.py")
    rommet = Rom()
    for i in range(3):
        rommet.legg_til_pære(Lyspære())

    rommet.skru_på_lys()