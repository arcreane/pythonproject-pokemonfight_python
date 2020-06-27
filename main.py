import pygame
from game import Game
from player import Player
from characters.pokemon import *
from fight import Fight
pygame.init()
pygame.font.init()
pygame.mixer.init()

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
rects = list()
while running:
    if not game.is_playing:
        # Set le background
        screen.blit(background, (0, 0))
        screen.blit(start_btn, (0, 0))

        # Mettre à jour l'écran
        pygame.display.flip()
    if game.fight and game.fight.is_over:
        game.playVictorySound()
        end_img = pygame.image.load('assets/Images/congratulations.jpg')
        screen.blit(end_img, (0, 0))
        starter_img = game.images[str(player.starter.Name) + '_hd']
        #starter_img = pygame.transform.scale(starter_img, (224, 224))
        screen.blit(starter_img, (550, 200))
        pygame.display.flip()
    # Si la fenêtre est fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn_rect != False and start_btn_rect.collidepoint(event.pos):
                player = Player('player')
                game.is_playing = True
                starterList = game.update_screen()
                start_btn_rect = False
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
                else:
                    break
                rects = game.fight.initFight()
                starterList = list()
            elif game.fight and isinstance(game.fight, Fight):
                if rects[0].collidepoint(event.pos):
                    game.fight.fighting(0)
                elif rects[1].collidepoint(event.pos):
                    game.fight.fighting(1)
