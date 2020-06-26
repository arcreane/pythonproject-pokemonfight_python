import pygame
from fight import Fight
from characters.pokemon import Rattata

class Game:
    def __init__(self, screen, font):
        self.fight = ''
        self.is_playing = False
        self.state = 0
        self.screen = screen
        self.myfont = font
        self.images = {'white_bg': pygame.image.load('assets/Images/white_screen.jpg'),
                       'Salamèche': pygame.image.load('assets/Sprites/salameche.png'),
                       'Salamèche_dos': pygame.image.load('assets/Sprites/salameche_dos.png'),
                       'Bulbizarre': pygame.image.load('assets/Sprites/bulbizarre.png'),
                       'Carapuce': pygame.image.load('assets/Sprites/carapuce.png'),
                       'rattata': pygame.image.load('assets/Sprites/rattata.png'),
                       'fight_bg': pygame.image.load('assets/Images/fight_bg.jpg')}

    def update_screen(self, starter=''):
        if self.state == 0:
            self.screen.blit(self.images['white_bg'], (0, 0))
            pygame.display.flip()
            textSurface = self.myfont.render("Choisissez un starter !", False, (0, 0, 255), (255, 255, 255))
            self.screen.blit(textSurface, (400, 114))
            starter_1 = pygame.transform.scale(self.images['Salamèche'], (112, 112))
            starter_1_rect = starter_1.get_rect()
            starter_1_rect.left = 469
            starter_1_rect.top = 214
            self.screen.blit(starter_1, (469, 214))
            starter_2 = pygame.transform.scale(self.images['Bulbizarre'], (112, 112))
            starter_2_rect = starter_2.get_rect()
            starter_2_rect.left = 669
            starter_2_rect.top = 214
            self.screen.blit(starter_2, (669, 214))
            starter_3 = pygame.transform.scale(self.images['Carapuce'], (112, 112))
            starter_3_rect = starter_3.get_rect()
            starter_3_rect.left = 269
            starter_3_rect.top = 214
            self.screen.blit(starter_3, (269, 214))
            pygame.display.flip()
            self.state = 1
            return {'Salamèche': starter_1_rect, 'Bulbizarre': starter_2_rect, 'Carapuce': starter_3_rect}
        elif self.state == 1:
            self.screen.blit(self.images['white_bg'], (0, 0))
            pygame.display.flip()
            self.screen.blit(self.images['fight_bg'], (0, 0))
            pygame.display.flip()
            self.fight = Fight(starter, Rattata(), self)






