import pygame

class Fight:
    def __init__(self, starter_pkmn, opponent_pkmn, currentGame):
        self.is_over = False
        self.starter = starter_pkmn
        self.opponent = opponent_pkmn
        self.game = currentGame

    def atck_display(self):
        pygame.draw.rect(self.game.screen, (255, 255, 255), (100, 388, 850, 100), 10)
        atck1_rect = pygame.draw.rect(self.game.screen, (255, 255, 255), (200, 408, 300, 60))
        atck1_name = self.game.myfont.render(self.starter.listAttack[0].Name, False, (0, 0, 255))
        self.game.screen.blit(atck1_name, (300, 425))
        atck2_rect = pygame.draw.rect(self.game.screen, (255, 255, 255), (550, 408, 300, 60))
        atck2_name = self.game.myfont.render(self.starter.listAttack[1].Name, False, (0, 0, 255))
        self.game.screen.blit(atck2_name, (640, 425))
        pygame.display.flip()
        return atck1_rect, atck2_rect

    def initFight(self):
        # Afficher barre de vie tout ça
        opponent_img = pygame.transform.scale(self.game.images['rattata'], (112, 112))
        self.game.screen.blit(opponent_img, (650, 200))
        starter_img = pygame.transform.scale(self.game.images[str(self.starter.Name) + '_dos'], (112, 112))
        self.game.screen.blit(starter_img, (275, 275))
        self.starter.health_update(self.game.screen, (240, 300))
        self.opponent.health_update(self.game.screen, (610, 210))
        pygame.display.flip()
        self.atck_display()
        return self.atck_display()

    def fighting(self, index):
        if not self.is_over:

            self.is_over = True

