class Skuff():
    def __init__(self) -> None:
        self._sokke_liste = []

    def sett_inn_sokk(self, sokk):
        self._sokke_liste.append(sokk)

    def sjekk_status(self):
        antall_høyre = 0
        antall_venstre = 0

        for sokk in self._sokke_liste:
            if sokk.hent_side() == "H":
                antall_høyre += 1
            if sokk.hent_side() == "V":
                antall_venstre += 1

            if antall_høyre == antall_venstre:
                print('Alt i orden')
            else:
                print('Ulikt antall høyre- og venstresokker.')
    