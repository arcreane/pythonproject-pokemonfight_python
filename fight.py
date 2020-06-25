import pygame

class Fight:
    def __init__(self, starter_pkmn, opponent_pkmn, currentGame):
        self.is_over = False
        self.starter = starter_pkmn
        self.opponent = opponent_pkmn
        self.game = currentGame
        self.initFight(self.opponent)


    def initFight(self, opponent):
        # Afficher barre de vie tout ça
        opponent_img = pygame.transform.scale(self.game.images['rattata'], (112, 112))
        self.game.screen.blit(opponent_img, (650, 200))
        print(self.starter.Name)
        starter_img = pygame.transform.scale(self.game.images[str(self.starter.Name) + '_dos'], (112, 112))
        self.game.screen.blit(starter_img, (275, 275))
        pygame.display.flip()
        self.fighting()
        pass

    def fighting(self):
        while not self.is_over:

            self.is_over = True

