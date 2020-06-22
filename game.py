import pygame


class Game:
    def __init__(self, screen):
        self.is_playing = False
        self.is_over = False
        self.state = 0
        self.screen = screen
        self.images = {'white_bg': pygame.image.load('assets/Images/white_screen.jpg')}

    def update_screen(self):
        if self.state == 0:
            self.screen.blit(self.images['white_bg'], (0, 0))
            pygame.display.flip()
            self.state == 1
        #elif self.state == 1:





