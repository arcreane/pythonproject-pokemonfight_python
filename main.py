import pygame
pygame.init()


# Générer la fenêtre de jeu
## Titre , icône (à rajouter plus tard si possible)
pygame.display.set_caption('Pokémon Fight')
screen = pygame.display.set_mode((1050, 540))

running = True

#background du jeu
background = pygame.image.load('assets/Images/fight_bg.jpg')

while running:

    # Set le background
    screen.blit(background, (0, 0))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si la fenêtre est fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()