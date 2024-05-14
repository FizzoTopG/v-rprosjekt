import pygame

# 1. Oppsett
pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 25)
overskrift_surface = overskrift_font.render("Greta vs Biler med V8", True, "gray")

spiller_surface = pygame.image.load("bilder/pixel-r8.png").convert_alpha()
spiller_surface = pygame.transform.scale_by(spiller_surface, 0.275)
spiller_rect = spiller_surface.get_rect()
spiller_rect.bottom = HOYDE
spiller_rect.centerx = BREDDE / 2
spiller_fart = 0

fiende_surface = pygame.image.load("bilder/pixel.greta.png").convert_alpha()
fiende_surface = pygame.transform.scale_by(fiende_surface, 0.2)
fiende_rect = fiende_surface.get_rect()
fiende_rect.top = 100
fiende_rect.centerx = BREDDE / 2

pollen_surface = pygame.image.load("bilder/pixel.forrurensing.png").convert_alpha()
pollen_surface = pygame.transform.scale_by(pollen_surface, 0.1)
pollen_rect = pollen_surface.get_rect()
pollen_rect.top = fiende_rect.bottom
pollen_rect.centerx = fiende_rect.centerx
pollen_fart = 1

while True:
    # 2. Håndtere input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if hendelse.type == pygame.KEYDOWN:
            if hendelse.key == pygame.K_LEFT:
                spiller_fart  = -1
            elif hendelse.key == pygame.K_RIGHT:
                spiller_fart = 1
        if hendelse.type == pygame.KEYUP:
            spiller_fart = 0
                

    # 3. oppdatere spill
    fiende_rect.left -=1
    if fiende_rect.right < 0:
        fiende_rect.left = BREDDE

    spiller_rect.left += spiller_fart
    pollen_rect.top += pollen_fart

    if pollen_rect.top > HOYDE:
        pollen_rect.top = fiende_rect.bottom
        pollen_rect.centerx = fiende_rect.centerx
        pollen_fart += 1

    if spiller_rect.colliderect(pollen_rect):
        pygame.quit()
        raise SystemExit 

    # 4. tegne
    vindu.fill("white")
    vindu.blit(overskrift_surface,(10,10))

    vindu.blit(spiller_surface, spiller_rect)
    vindu.blit(fiende_surface, fiende_rect)

    vindu.blit(pollen_surface, pollen_rect)

    pygame.display.flip()
    klokke.tick(FPS)