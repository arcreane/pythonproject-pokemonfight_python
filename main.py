import pygame
pygame.init()


# Générer la fenêtre de jeu
## Titre , icône (à rajouter plus tard si possible)
pygame.display.set_caption('Pokémon Fight')
pygame.display.set_mode((1080, 720))

running = True


while running:

    # Si la fenêtre est fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()