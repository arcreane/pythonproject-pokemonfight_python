import pygame
from game import Game
from player import Player
from characters.pokemon import *
pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('assets/Fonts/VT323/VT323-Regular.ttf', 36)


# Générer la fenêtre de jeu
## Titre , icône (à rajouter plus tard si possible)
pygame.display.set_caption('Pokémon Fight')
screen = pygame.display.set_mode((1050, 540))

running = True

#background du jeu
screen.fill((255, 255, 255))
background = pygame.image.load('assets/Images/pkmn_fight.png')
start_btn = pygame.image.load('assets/Images/start_btn.png')

# Récupérer zone cliquable du boutton start
start_btn_rect = start_btn.get_rect()
start_btn_rect.top = 418
start_btn_rect.left = 404
start_btn_rect.height = 52
start_btn_rect.width = 279

game = Game(screen, myfont)
starterList = list()
while running:
    if not game.is_playing:
        # Set le background
        screen.blit(background, (0, 0))
        screen.blit(start_btn, (0, 0))

        # Mettre à jour l'écran
        pygame.display.flip()

    # Si la fenêtre est fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn_rect.collidepoint(event.pos):
                player = Player('player')
                game.is_playing = True
                starterList = game.update_screen()
            elif starterList:
                if starterList['Salamèche'].collidepoint(event.pos):
                    player.starter = Salamèche()
                    game.update_screen(player.starter)
                elif starterList['Bulbizarre'].collidepoint(event.pos):
                    player.starter = Bulbizarre()
                    game.update_screen(player.starter)
                elif starterList['Carapuce'].collidepoint(event.pos):
                    player.starter = Carapuce()
                    game.update_screen(player.starter)