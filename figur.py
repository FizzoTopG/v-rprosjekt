import pygame

class Figur():
    def __init__(self, bildesti: str) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()


    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)
        # pygame.draw.rect(vindu, (255,0,0), pygame.rect.Rect(self.ramme.centerx-9 , self.ramme.bottom - 5, 18, 5))
        # pygame.draw.rect(vindu, (255, 0, 0), self.ramme, 2) 