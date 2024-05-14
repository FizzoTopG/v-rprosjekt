import pygame
import pygame.freetype
from tilstand import Tilstand 

class Hovedmeny(Tilstand):
    def __init__(self, vindu_bredde: int, vindu_høyde: int, menyvalg: list) -> None:
        super().__init__(vindu_bredde, vindu_høyde)
        self.tittel_font = pygame.freetype.SysFont("serif", 128)
        self.meny_font = pygame.freetype.SysFont("sans", 64)
        self.peker_posisjon = 0
        self.menyvalg = menyvalg

    def håndter_input(self):
        pass

    def tegn(self, vindu: pygame.Surface):
        self.overflate.fill("blue") # Fyller hele meny-overflaten med blå
        vindu.blit(self.overflate,self.ramme) # Tegner hele menyen i vinduet

    def kjør(self):
        self.håndter_input()
        self.tegn()