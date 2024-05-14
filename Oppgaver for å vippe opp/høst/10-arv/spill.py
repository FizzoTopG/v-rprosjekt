import pygame
from fotballspiller import Fotballspiller
from ball import Ball
import random

# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

spiller = Fotballspiller(BREDDE, HOYDE)
ball = Ball(BREDDE)

overskrift_font = pygame.font.SysFont("Arial", 25)

spiller.bilde = pygame.transform.scale_by(spiller.bilde, 0.1)
spiller.ramme.y = 550

ball.bilde = pygame.transform.scale_by(ball.bilde, 0.7)

while True:
    
    


    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    if spiller.ramme.colliderect(ball.ramme):
        spiller.poeng += 1
        ball.ramme.y = 0
        ball.ramme.x = random.randint(0, 600)
    
        
        
        
        
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt(-3)
    if taster[pygame.K_RIGHT]:
        spiller.flytt(3)

    # 3. Oppdater spill
    ball.fall(HOYDE)


    # 4. Tegn
    vindu.fill("black")
    overskrift_surface = overskrift_font.render(str(spiller.poeng), True, "white")
    vindu.blit(overskrift_surface, (0,0))
    spiller.tegn(vindu)
    ball.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)