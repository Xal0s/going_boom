import pygame

# Définition des couleurs et initialisation de Pygame
COULEUR_FOND = (255, 255, 255)
ORANGE = (237, 127, 16)
WHITE = (255, 255, 255)
pygame.init()

# Initialisation de la fenêtre et des ressources
fond = pygame.image.load("fond.jpg")
LARGEUR, HAUTEUR = fond.get_size()
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)
fond = fond.convert()

LARGEUR_REC = 120
HAUTEUR_REC = 50

police = pygame.font.Font("police.ttf", 16)
msg_clic = police.render("Clique ici", True, WHITE)

joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

regles = pygame.image.load("regles.png").convert()
petit_regles = pygame.transform.scale(regles, (regles.get_width() // 1.6, regles.get_height() // 1.6))
petit_regles = petit_regles.convert_alpha()

etat_jeu = "debut"
print(etat_jeu)
presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

rect_orange = pygame.draw.rect(fen, ORANGE, [246, 40, LARGEUR_REC, HAUTEUR_REC])

def afficher_elements_begin():
    fen.blit(fond, (0, 0))
    fen.blit(petit_joueur, (420, 20))
    fen.blit(petit_regles, (40, 140))
    fen.blit(petit_presentateur, (120, 20))
    pygame.draw.rect(fen, ORANGE, [246, 40, LARGEUR_REC, HAUTEUR_REC])  # Dessin du rectangle
    fen.blit(msg_clic, (255, 55))
    pygame.display.flip()

def gerer_evenements_begin():
    global etat_jeu
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if rect_orange.collidepoint(event.pos):
                    etat_jeu = "choix_difficultes"
                    print(etat_jeu)
        afficher_elements_begin()

def main():
    global etat_jeu
    afficher_elements_begin()
    gerer_evenements_begin()
    pygame.quit()

if __name__ == "__main__":
    main()
