import pygame

from figur import Figur

class Blokk():
    def __init__(self, midtx, midty, antall) -> None:
        self.bilde = pygame.transform.scale_by(pygame.image.load("bilder/mario-sprite.png").convert_alpha(), 0.1)
        self.ramme = self.bilde.get_rect()
        self.ramme.width = self.ramme.width * antall
        self.ramme.centerx = midtx
        self.ramme.centery = midty
        self.antall = antall


    def tegn(self, vindu):
        for i in range(self.antall):
            vindu.blit(self.bilde, pygame.rect.Rect(self.ramme.left + self.ramme.height * i, self.ramme.top, self.ramme.height, self.ramme.height))