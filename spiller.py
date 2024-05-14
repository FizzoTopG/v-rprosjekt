import pygame

from figur import Figur

class Spiller(Figur):
    def __init__(self, sprite: str,  bildesti: str, vindu_bredde: int, vindu_høyde:int ) -> None:
        super().__init__(bildesti)
        self.poeng = 0
        self.kollidert = False
        # Legg til vindu_bredde og vindu_høyde i init-metoden
        self.vindu_bredde = vindu_bredde  
        self.vindu_høyde = vindu_høyde

        # Fart

        self.fart_y = 0
        self.acc_y = 0.6
        
        

        # FOR ANIMATION
        # HENTER EN STARTSTID
        self.update_time = pygame.time.get_ticks()
        # LASTER BILDER
        self.runningsheet = pygame.transform.scale_by(pygame.image.load(sprite).convert_alpha(), 2)
        self.standing = pygame.transform.scale_by(pygame.image.load(bildesti).convert_alpha(), 2)
        # ANGIR HVOR LENGE DET ER MELLOM HVER ANIMASJON
        self.animation_delay = 20
        # GJØR AT ANIMASJONEN STARTER PÅ FØRSTE BILDE
        self.frame_index = 0
        self.last_dir = None
        self.ramme = self.standing.get_rect()

        #setter spiler i startposisjon
        self.ramme.centerx = vindu_bredde
        self.ramme.bottom = vindu_høyde 

    def load_animations(self):
        # HENTER HØYDE OG BREDDE PÅ MANNEN
        man_height = self.runningsheet.get_height()
        man_width = self.runningsheet.get_width()/10
        animation_list = []
        for i in range(10):
            # LAGER ET MIDLERTIDIG BILDE OG LEGGER DET TIL I LISTEN
            # BILDENE ER LAGET AV EN DEL AV ET SPRITESHEET
            temp_img = self.runningsheet.subsurface(man_width * i + 9 - i, 0, man_width, man_height)
            animation_list.append(temp_img)
        return animation_list

    def play_animation(self):
        animation_list = self.load_animations()
        self.animation_list = animation_list
        # SJEKKER HVILKEN RETNING SPILLEREN BEVEGER/BEVEGDE SEG
        if self.last_dir == "l":
            # SJEKKER OM DET HAR GÅTT LANG NOK TID TIL AT DEN SKAL ENDRES
            if pygame.time.get_ticks() - self.update_time > self.animation_delay:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # SJEKKER OM frame_index ER I REKKEVIDDEN TIL LISTEN
            if self.frame_index >= len(animation_list):
                self.frame_index = 0
            # FLIPPER BILDET RIKTIG VEI
            self.bilde = pygame.transform.flip(animation_list[self.frame_index], 1, 0)
        elif self.last_dir == "r":
            # SAMME SOM FORRIGE
            if pygame.time.get_ticks() - self.update_time > self.animation_delay:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(animation_list):
                self.frame_index = 0
            self.bilde = animation_list[self.frame_index]
        else:
            # ANGIR HVORDAN BILDET ER DERSOM PERSONEN IKKE BEVEGER SEG
            if self.last_dir == "r_":
                self.bilde = self.standing
            else:
                self.bilde = pygame.transform.flip(self.standing, 1, 0)


    def står(self, blokk_liste):
        for blokk in blokk_liste:
            if pygame.rect.Rect(self.ramme.centerx - 9 , self.ramme.bottom - 5, 18, 5).colliderect(blokk.ramme):
                self.ramme.bottom = blokk.ramme.top + 5
                return True
        return False

    def oppdater(self, blokk_liste):
        # oppdaterer posisjon, bilde og tilstand til karakteren
        if self.står(blokk_liste) and self.fart_y >= 0:
            self.fart_y = 0
        else:
            self.fart_y += self.acc_y
            if self.fart_y >= 20:
                self.fart_y = 20
            self.ramme.top += self.fart_y
            self.play_animation()



    def flytt(self, dx: int):
        self.ramme.x += dx