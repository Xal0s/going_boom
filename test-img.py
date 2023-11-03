import pygame

#Couleurs qui seront utilisés dans le jeu
VERT = (0, 153, 51)
ORANGE = (255, 255, 255)
VERTB = (0, 204, 0)
VIOLET = (102, 0, 102)
WHITE = (255, 255, 255)
COULEUR_COMPTEUR = (53, 200, 23)
COULEUR_FOND = (255, 255, 255)

# FPS = frame per second (images par seconde)
FPS = 50
compteur_frame = 0
timer = 120
#appel des fonctions de pygame
pygame.init()

#font utiliser dans le jeu
police = pygame.font.Font("AAhaWow-2O1K8.ttf", 30)

#appel du temps par la fonction time de pygame
horloge = pygame.time.Clock()

# Chargement de l'image du fond
fondjeu = pygame.image.load("fond.jpg")
print("Dimension de l'image de fond", fondjeu.get_size())
fondjeu.set_alpha(200)

# Les dimensions de la fenêtre sont celles de l'image du fond
LARGEUR, HAUTEUR = fondjeu.get_size()
#Dimensions du rectangle de questions/reponses
LARGEUR_REC = 572
HAUTEUR_REC = 80

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)

# Préparation de de l'image du bambou à son utilisation dans pygame
fondjeu = fondjeu.convert()

# Chargement et préparation des sprites utilisés
joueur = pygame.image.load("joueur.png").convert()
print("Dimension de l'image du joueur", joueur.get_size())

petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 9, joueur.get_height() // 9))
petit_joueur = petit_joueur.convert_alpha()

presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))# Remplace la couleur (0, 0, 0) - Noir en transparence

petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 13, presentateur.get_height() // 13))
petit_presentateur = petit_presentateur.convert_alpha()
print("Dimension de l'image du presentateur", presentateur.get_size())

bomb_images = [pygame.image.load(f"bombe_{i}.svg").convert_alpha() for i in range(1, 11)]
reduced_bomb_images = [pygame.transform.scale(image, (image.get_width() // 3, image.get_height() // 3)) for image in bomb_images]

explosion = pygame.image.load("fire-5518.gif")

question_index = 0
reponse = ""

#nos questions
questions = [
    "Quelle est la capitale de la France ?",
    "Quel est le plus grand océan du monde ?",
    "Qui a peint la Joconde ?",
]
#nos réponses
reponses = ["Paris", "Océan Pacifique", "Leonard de Vinci"]
etat_reponse = None
#choix de la taille de caractère et la font du texte ecrit dans l'interface
font = pygame.font.Font("AAhaWow-2O1K8.ttf", 20)
#variable pour que la question s'affiche dans l'interface
texte_question = font.render(questions[question_index], True, (255, 11, 11))
#definition de la position du rectangle dans lequel la question apparaitra
rect_question = texte_question.get_rect(center = (300, 320)) 
verdict = font.render(etat_reponse, True, (0, 255, 0))

continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            print(reponse)
            if event.key == pygame.K_BACKSPACE:
                print("suppr")
                #on supprime le dernier element de la liste qui contient la reponse de l'utilisateur
                reponse = reponse[:-1]
                print(reponse)
             #si on appuie sur 'entrer'
            elif event.key == pygame.K_RETURN:
                if reponse.lower() == reponses[question_index].lower():
                    etat_reponse = "Bonne réponse"
                    question_index += 1
                    print(etat_reponse)
                else:
                    etat_reponse = "Mauvaise réponse"
                    timer -= 5
                    print(verdict, (0,0))                    
                reponse = ""
                #si l'entrée de l'utilisateur contient quelque chose
                
                if question_index < len(questions):
                    texte_question = font.render(questions[question_index], True, (255, 11, 11))
                else:
                    print("Toutes les questions sont terminées.")
                    continuer = False
            elif event.unicode != '':
                #on l'ajoute a la variable reponse
                reponse += event.unicode
               
    if timer <= 0:
        fen.blit(explosion, (0,0))
        continuer = False
    
    
    # Affichage du fond aux coord9onnées précisées en second argument
    fen.blit(fondjeu, (0, 0))
    fen.blit(petit_joueur, (350, 100))
    #fen.blit(petit_bomb, (270, 220))
    fen.blit(petit_presentateur, (150, 120))
    
    pygame.draw.rect(fen, WHITE, [20, HAUTEUR - HAUTEUR_REC, LARGEUR_REC, HAUTEUR_REC])
    # Affichage de l'image correspondant à l'étape actuelle de la bombe
    index_image = max(0, (timer - 1) // 12)
    fen.blit(reduced_bomb_images[index_image], (270, 220))
    msg_compteur = police.render(f"{timer:02d}", True, COULEUR_COMPTEUR)
    fen.blit(msg_compteur, (270, 20))
    fen.blit(texte_question, rect_question)
                    
    texte_reponse = font.render(reponse, True, (0, 0, 0))
    #on definit le rectangle dans lequel la reponse s'affichera
    rect_reponse = texte_reponse.get_rect(center=(300, 350 ))
    #on affiche la saisie utilisateur
    fen.blit(texte_reponse, rect_reponse.topleft)

    pygame.display.flip()
    compteur_frame += 1
    if compteur_frame == FPS:
        timer -= 1
        compteur_frame = 0

    # Attente
    horloge.tick(FPS)
    


pygame.quit()

