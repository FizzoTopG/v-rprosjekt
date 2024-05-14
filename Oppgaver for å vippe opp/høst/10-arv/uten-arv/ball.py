import pygame
import random

class Ball():
    def __init__(self, vindu_bredde: int) -> None:
        self.bilde = pygame.image.load("bilder/ball.png").convert_alpha()
        self.ramme = self.bilde.get_rect()  

        #flytter ballen til startposisjonen
        self.ramme.centerx = random.randint(0, vindu_bredde) #ballen dukker opp et tilfeldig sted på bredden
        self.ramme.top = 0

    def fall(self, vindu_høyde: int):
        if self.ramme.top > vindu_høyde: 
            self.ramme.x += 0
        self.ramme.y += 1

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)