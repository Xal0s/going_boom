# Fenêtre de jeu de Going bomb

import pygame

VERT = (0, 153, 51)
ORANGE = (255, 153, 0)
VERTB = (0, 204, 0)
VIOLET = (102, 0, 102)
WHITE = (255, 255, 255)

# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)

# FPS = frame per second (images par seconde)
FPS = 1

pygame.init()

# Permettra d'attendre avant de rafraîchir l'affichage
police = pygame.font.Font("police.ttf", 30)

# Permettra d'attendre avant de rafraîchir l'affichage
horloge = pygame.time.Clock()

# Chargement de l'image du fond
fondjeu = pygame.image.load("fond.jpg")
print("Dimension de l'image de fond", fondjeu.get_size())
fondjeu.set_alpha(200)

# Les dimensions de la fenêtre sont celles de l'image du fond
LARGEUR, HAUTEUR = fondjeu.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)

# Préparation de de l'image du bambou à son utilisation dans pygame
fondjeu = fondjeu.convert()

COULEUR_COMPTEUR = (53, 200, 23)

LARGEUR_REC = 572
HAUTEUR_REC = 50

# Entre 0 (transparence totale) et 255 (aucune transparence)
#fondjeu.set_alpha(127)

# Chargement et préparation de l'image du panda
joueur = pygame.image.load("joueur.png").convert()
print("Dimension de l'image du joueur", joueur.get_size())

petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 9, joueur.get_height() // 9))
petit_joueur = petit_joueur.convert_alpha()

presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))  # Remplace la couleur (0, 0, 0) - Noir en transparence
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 13, presentateur.get_height() // 13))
petit_presentateur = petit_presentateur.convert_alpha()
print("Dimension de l'image du presentateur", presentateur.get_size())

bomb_images = [pygame.image.load(f"bombe_{i}.svg").convert_alpha() for i in range(1, 11)]
reduced_bomb_images = [pygame.transform.scale(image, (image.get_width() // 3, image.get_height() // 3)) for image in bomb_images]




compteur = 120

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
    
    if compteur == 0:
        continuer = False
    
    # Affichage du fond aux coord9onnées précisées en second argument
    fen.blit(fondjeu, (0, 0))
    fen.blit(petit_joueur, (350, 100))
    #fen.blit(petit_bomb, (270, 220))
    fen.blit(petit_presentateur, (150, 120))
    pygame.draw.rect(fen, ORANGE, [20, 323, LARGEUR_REC, HAUTEUR_REC])
    # Affichage de l'image correspondant à l'étape actuelle de la bombe
    index_image = max(0, (compteur - 1) // 12)
    fen.blit(reduced_bomb_images[index_image], (270, 220))
    msg_compteur = police.render(f"{compteur:02d}", True, COULEUR_COMPTEUR)
    fen.blit(msg_compteur, (270, 20))

    pygame.display.flip()
    
    compteur -= 1

    # Attente
    horloge.tick(FPS)
    


pygame.quit()

