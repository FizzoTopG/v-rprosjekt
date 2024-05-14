import pygame
from planet import Planet


#1 Oppsett
pygame.init()
BREDDE = 1000
HOYDE = 400
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()


Planeter = [

Planet(100,200, 50, "bilder/earth.png" ),
Planet(200,300, 100,"bilder/jupiter.png"),
Planet(400,200, 20, "bilder/saturn.png"),
Planet(600,200, 40, "bilder/uranus.png")

]

while True:
    #2. håndtere input
    for hendelse in pygame.event.get():
        pygame.quit()
        raise SystemExit
    
    # 3. Oppdatere spill

    # 4. Tegn
    for planet in Planeter:
        planet.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)