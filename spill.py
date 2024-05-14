import pygame, random

# Klasser
from spiller import Spiller
from blokk import Blokk
from flagg import Flagg


# 1. Oppsett
pygame.init()
BREDDE = 900
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift_font = pygame.font.SysFont("Arial", 25)

flammer = pygame.image.load("bilder/pxArt.png")
flammer = pygame.transform.scale_by(flammer, 0.3)
flammerramme = flammer.get_rect()



flagg = Flagg(BREDDE)
flagg.bilde = pygame.transform.scale_by(flagg.bilde, 0.3)


spiller = Spiller("bilder/running_sprite.png","bilder/standing.png",BREDDE/90, HOYDE*11/12)
spiller2 = Spiller( "bilder/running_spirte2.png","bilder/standing2.png", BREDDE/90, HOYDE*11/12)



blokk_liste = [
    Blokk(0,560,900),
    Blokk(800, 475, 5),
    Blokk(550, 400, 3),
    Blokk(350, 400, 3),
    Blokk(150, 325, 5),
    Blokk(350, 250, 3),
    Blokk(550, 250, 3),
    Blokk(800, 175, 5)

]

blokk_liste2 = [
    Blokk(0,560,900),
    Blokk(125, 500, 3),
    Blokk(225, 425, 3),
    Blokk(125, 350, 3),
    Blokk(225, 275, 3),
    Blokk(125, 200, 3),
    Blokk(225, 125, 3),
    Blokk(325, 200, 3),
    Blokk(425, 275, 3),
    Blokk(525, 350, 3),
    Blokk(675, 350, 1),
    Blokk(800, 300, 6),
    Blokk(800, 175, 1)
]

blokk_liste3 = [Blokk(0,560,900),]


lister_blokker = [blokk_liste, blokk_liste2, blokk_liste3]



def vinne(vindu):
    font = pygame.font.SysFont(None, 70)
    if spiller.poeng == 3:
        text = font.render("GRATULERER BLÅ" , True, "BLUE")
    elif spiller2.poeng == 3:
        text = font.render("GRATULERER GUL" , True, "YELLOW")
    vindu.blit(text, (250, HOYDE / 2))
    pygame.display.update()




font = pygame.font.SysFont(None, 50)
def nedtelling(vindu):
    nedtelling_tid = 0
    if flagg.tatt and flagg.cooldown > 0:
        nedtelling_tid = flagg.cooldown // 60  # Konverter fra frames til sekunder
        tekst = font.render(f"{nedtelling_tid}", True, "Black")
        vindu.blit(tekst, (450, 10))


index = 0


while True:
    
        # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
            
    taster = pygame.key.get_pressed()
    # SJEKKER FORRIGE RETNINGEN PLAYER GIKK
    if spiller.last_dir == "r" or spiller.last_dir== "r_":
        spiller.last_dir = "r_"
    else:
        spiller.last_dir = "l_"

    if spiller2.last_dir == "r" or spiller2.last_dir== "r_":
        spiller2.last_dir = "r_"
    else:
        spiller2.last_dir = "l_"
    

    if flagg.cooldown <= 0:
        if taster[pygame.K_LEFT] and taster[pygame.K_RIGHT] :
            pass
        if taster[pygame.K_a] and taster[pygame.K_d]:
            pass
        if taster[pygame.K_LEFT]:
            if spiller.ramme.left >= 0:
                spiller.flytt(-5)
                spiller.last_dir = "l"

        if taster[pygame.K_RIGHT]:
            if spiller.ramme.right <= BREDDE:
                spiller.flytt(5)
                spiller.last_dir = "r"

        if taster[pygame.K_SPACE] or taster[pygame.K_UP]:
                if spiller.står(blokk_liste) and spiller.fart_y > -1:
                    spiller.fart_y = -11
            

        if taster[pygame.K_a]:
            if spiller2.ramme.left >= 0:
                spiller2.flytt(-5)
            spiller2.last_dir = "l"

        if taster[pygame.K_d]:
            if spiller2.ramme.width <= BREDDE:
                spiller2.flytt(5)
                spiller2.last_dir = "r"

        if taster[pygame.K_w]:
                if spiller2.står(blokk_liste) and spiller2.fart_y > -1:
                    spiller2.fart_y = -11

        
    if flagg.tatt == False:
        if spiller.ramme.colliderect(flagg.ramme):
            spiller.poeng += 1
            flagg.tatt = True
            flagg.cooldown = 300
            spiller.ramme.centerx = BREDDE/90
            spiller.ramme.bottom = HOYDE*11/12
            spiller2.ramme.centerx = BREDDE/90
            spiller2.ramme.bottom = HOYDE*11/12
            
        if spiller2.ramme.colliderect(flagg.ramme):
            spiller2.poeng += 1
            flagg.tatt = True
            flagg.cooldown = 300
            spiller.ramme.centerx = BREDDE/90
            spiller.ramme.bottom = HOYDE*11/12
            spiller2.ramme.centerx = BREDDE/90
            spiller2.ramme.bottom = HOYDE*11/12
    else: 
        if flagg.cooldown > 0:
            flagg.cooldown -= 1
        else:
            flagg.tatt = False

        
    if spiller.poeng == 3 or spiller2.poeng == 3:
        vinne(vindu)
        pygame.time.delay(2000) 
        index += 1
        if index == 2:
            pygame.quit()
            raise SystemExit
        blokk_liste = lister_blokker[index]
        spiller.poeng = 0
        spiller2.poeng = 0
        




    # 3. Oppdater spill
    spiller.play_animation()
    spiller.oppdater(blokk_liste)    

    spiller2.play_animation()
    spiller2.oppdater(blokk_liste)    
        

        # 4. Tegn
    vindu.fill((65, 105, 255))
    for blokk in blokk_liste2:
        blokk.tegn(vindu)
    for i in range(9):
        flammerramme.topleft = (100 * i, 560)
        vindu.blit(flammer, flammerramme)

    overskrift_surface = overskrift_font.render("Gul: " + str(spiller2.poeng), True, "white")
    overskrift_surface2 = overskrift_font.render("Blå: " + str(spiller.poeng), True, "white")
    vindu.blit(overskrift_surface, (200,0))
    vindu.blit(overskrift_surface2, (600,0))

    if flagg.tatt == False:
            flagg.tegn(vindu)

    spiller.tegn(vindu)
    spiller2.tegn(vindu)
    nedtelling(vindu)

    pygame.display.flip()
    klokke.tick(FPS)
   