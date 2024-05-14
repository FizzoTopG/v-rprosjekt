import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1000
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)

dino_x = 300
dino_y = 500
dino_bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha()

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_RIGHT]:
        print("Pil høyre")
        dino_x += 2

    if taster[pygame.K_LEFT]:
        print("Pil left")
        dino_x -= 2

    if taster[pygame.K_DOWN]:
        print("Pil ned")
        dino_y += 2

    if taster[pygame.K_UP]:
        print("Pil opp")
        dino_y -= 2

    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit

    # 3. Oppdater spill
    # 4. Tegn
    vindu.fill("grey")
    # vindu.fill((255,10,0))

    # pygame.draw.rect(vindu, (255,255,255), (0,220,1000,70))
    # pygame.draw.rect(vindu, (255,255,255), (300,0,70,600))

    

    vindu.blit(dino_bilde1,(dino_x,dino_y))

    tekst_lykke_til = stor_font.render("Lykke til!", True, "blue" )
    vindu.blit(tekst_lykke_til, (10,10))


    print("En runde i gameloopen")
    pygame.display.flip()
    klokke.tick(FPS)