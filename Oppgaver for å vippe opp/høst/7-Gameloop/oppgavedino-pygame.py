import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1000
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 34)
liten_font = pygame.font.SysFont("Arial", 12)

dino_x = 100
dino_y = 300
dino1 = pygame.image.load("bilder/dino1.png").convert_alpha()


sirkel1_x = 500
sirkel1_y = 200
sirkel1_farge = "green"

sirkel2_x = 400
sirkel2_y = 300
sirkel2_farge = "green"

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    
    taster = pygame.key.get_pressed()
    if taster[pygame.K_RIGHT]:
        print("Pil høyre")
        dino_x += 10

    if taster[pygame.K_LEFT]:
        print("Pil left")
        dino_x -= 10

    if taster[pygame.K_DOWN]:
        print("Pil ned")
        dino_y += 10

    if taster[pygame.K_UP]:
        print("Pil opp")
        dino_y -= 10

    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit
   
    # 3. Oppdater spill
    dino_rektangel = pygame.Rect(dino_x,dino_y, 100, 100)
    sirkel1_rektangel = pygame.Rect(sirkel1_x, sirkel1_y, 80, 80)
    sirkel2_rektangel = pygame.Rect(sirkel2_x, sirkel2_y, 80, 80)

    if dino_rektangel.colliderect(sirkel1_rektangel):
        print("over sirkel1")
        sirkel1_farge = "red"

    if dino_rektangel.colliderect(sirkel2_rektangel):
        print("over sirkel2")
        sirkel2_farge = "red"

    # 4. Tegn
    vindu.fill("white")
    vindu.blit(dino1, (dino_x,dino_y))

  

    pygame.draw.circle(vindu, sirkel1_farge, (sirkel1_x, sirkel1_y), 40)
    pygame.draw.circle(vindu, sirkel2_farge, (sirkel2_x, sirkel2_y), 35)

    dinotekst = stor_font.render("DINO", True, "blue" )
    vindu.blit(dinotekst, (150,50))



    pygame.display.flip()
    klokke.tick(FPS)