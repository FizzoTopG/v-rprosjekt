
from figur import Figur
import pygame

class Flagg(Figur):
    def __init__(self, vindu_bredde: int) -> None:
        super().__init__("bilder/flagg.png")
        self.tatt = False
        self.cooldown = -1
        self.ramme.topleft = (740,0)

        ny_bredde = int(self.ramme.width * 0.3)
        ny_hoyde = int(self.ramme.height * 0.3)
        self.ramme.inflate_ip(ny_bredde - self.ramme.width, ny_hoyde - self.ramme.height)


