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
        self.starter.health_update(self.game.screen, (240, 250), self.starter.HP)
        self.opponent.health_update(self.game.screen, (610, 160), self.opponent.HP)
        pygame.display.flip()
        self.atck_display()
        pygame.mixer.music.load('assets/Songs/fight.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(0)
        return self.atck_display()

    def fighting(self, index):
        if not self.is_over:
            if self.starter.Speed >= self.opponent.Speed:
                #fonction attaque du starter
                self.starter_atck(index)
                if self.is_over:
                    return
                pygame.time.wait(750)
                #fonction attaque de l'adversaire
                self.counter_atck()
                if self.is_over:
                    return
            else:
                # fonction attaque de l'adversaire
                self.counter_atck()
                if self.is_over:
                    return
                # fonction attaque du starter
                self.starter_atck(index)
                if self.is_over:
                    return
            #self.is_over = True

    def starter_atck(self, index):
        damage = (8 * self.starter.Attack * self.starter.listAttack[index].Value) / (self.opponent.Defense * 50) + 2
        self.opponent.HP -= damage
        if self.opponent.HP < 0:
            self.opponent.HP = 0
        self.opponent.health_update(self.game.screen, (610, 160), self.opponent.HP)
        pygame.display.flip()
        if self.opponent.HP == 0:
            self.is_over = True


    def counter_atck(self):
        damage = (8 * self.opponent.Attack * self.opponent.listAttack[0].Value) / (self.starter.Defense * 50) + 2
        self.starter.HP -= damage
        if self.starter.HP < 0:
            self.starter.HP = 0
        self.starter.health_update(self.game.screen, (240, 250), self.starter.HP)
        pygame.display.flip()
        if self.starter.HP == 0:
            self.is_over = True


