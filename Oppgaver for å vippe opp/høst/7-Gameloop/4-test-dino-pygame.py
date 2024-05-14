import pygame

# 1. Oppsett
pygame.init()

BREDDE = 600
HOYDE = 400
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 34)
liten_font = pygame.font.SysFont("Arial", 12)

gravitasjon = 0.1
dino_x = 300
dino_y = 0
dino_y_fart = 0
dino1 = pygame.image.load("bilder/dino1.png").convert_alpha()
dino2 = pygame.image.load("bilder/dino2.png").convert_alpha()

bakgrunn = pygame.image.load("bilder/bakgrunn.png").convert_alpha()
bakgrunn_x = 0
bakgrunn_y = 300



while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        dino_y_fart = -2
    dino_y += dino_y_fart


    # 3. Oppdater spill
    
    bakgrunn_x -=1
    if bakgrunn_x < - 300:
        bakgrunn_x = 0

    if dino_y > 200:
        dino_y_fart = 0
    else:
        dino_y_fart += gravitasjon
        dino_y += dino_y_fart


    # 4. Tegn
    vindu.fill("white")
    vindu.blit(bakgrunn, (bakgrunn_x,bakgrunn_y))


    vindu.blit(dino1, (dino_x,dino_y))
    vindu.blit(dino2, (dino_x,dino_y))




    pygame.display.flip()
    klokke.tick(FPS)