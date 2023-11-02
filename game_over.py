import pygame

COULEUR_FOND = (255, 255, 255)
ORANGE = (237, 127, 16)
WHITE = (255, 255, 255)
pygame.init()

fond = pygame.image.load("fond.jpg")
LARGEUR, HAUTEUR = fond.get_size()
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)
fond = fond.convert()

LARGEUR_REC = 120
HAUTEUR_REC = 50

police = pygame.font.Font("police.ttf", 16)
msg_replay = police.render("REPLAY", True, WHITE)

joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

game_over = pygame.image.load("game_over.png").convert()
petit_game_over = pygame.transform.scale(game_over, (game_over.get_width() // 1.3, game_over.get_height() // 1.3))
petit_game_over = petit_game_over.convert_alpha()

explo = pygame.image.load("explosion.gif").convert()
petit_explo = pygame.transform.scale(explo, (explo.get_width() // 5, explo.get_height() // 5))
petit_explo = petit_explo.convert_alpha()

etat_jeu = "choix_difficultes"
presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))  
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

# Définition des rectangles
rect_orange = pygame.Rect(246, 40, LARGEUR_REC, HAUTEUR_REC)

# Affichage des éléments à l'écran
def afficher_elements_game_over():
    fen.blit(fond, (0, 0))
    fen.blit(petit_joueur, (420, 20))
    fen.blit(petit_explo, (420, 140))
    fen.blit(petit_game_over, (195, 140))
    fen.blit(petit_presentateur, (120, 20))
    fen.blit(petit_explo, (50, 140))
    pygame.draw.rect(fen, ORANGE, rect_orange)
    fen.blit(msg_replay, (272, 57))
    pygame.display.flip()

# Gestion des événements et logique du jeu
def gerer_evenements_game_over():
    global etat_jeu
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if rect_orange.collidepoint(event.pos):
                    etat_jeu = "choix_difficultes"
                    print(" --> Replay")
                    print(etat_jeu)
        afficher_elements_game_over()

# Fonction principale
def main():
    global etat_jeu
    afficher_elements_game_over()
    gerer_evenements_game_over()
    pygame.quit()

if __name__ == "__main__":
    main()
