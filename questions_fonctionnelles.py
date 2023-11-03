import pygame
#couleur du background de la fenetre
couleur_fond = (255, 255, 255)
#taille de l'interface
largeur = 1000
hauteur = 500
#initialisation du jeu
pygame.init()
#création de la fenetre de l'interface
fen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Questions de culture générale")
#on rempli la fenetre avec la couleur de background
fen.fill(couleur_fond)
#variable pour determiner si on reste dans la boucle while infini ou non
continuer = True
#nos questions
questions = [
    "Quelle est la capitale de la France ?",
    "Quel est le plus grand océan du monde ?",
    "Qui a peint la Joconde ?",
]
#nos réponses
reponses = ["Paris", "Océan Pacifique", "Leonard de Vinci"]
#variable pour savoir quelle question sera posé
question_index = 0
#champ de saisie de l'utilisateur
reponse = ""
# Variable pour suivre l'état de la réponse
etat_reponse = None
# Message à afficher
message_reponse = ""  

#choix de la taille de caractère et la font du texte ecrit dans l'interface
font = pygame.font.Font(None, 36)
#variable pour que la question s'affiche dans l'interface
texte_question = font.render(questions[question_index], True, (255, 0, 0))
#definition de la position du rectangle dans lequel la question apparaitra
rect_question = texte_question.get_rect(center = (500, hauteur - 150))  

#on entre dans la boucle while infini
while continuer:
    #on stock dans la variable 'event' tous les evenements que l'on recupere
    for event in pygame.event.get():
        #si l'utilisateur appuie sur la croix de la fenetre d'interface
        if event.type == pygame.QUIT:
            #on sort de la boucle infini
            continuer = False
        #si le type d'evenement est une touche pressée
        elif event.type == pygame.KEYDOWN:
            #si la réponse n'est pas validée
            if not etat_reponse:
                #lorsqu'on appuie sur 'backspace'
                if event.key == pygame.K_BACKSPACE:
                    print("suppr")
                    #on supprime le dernier element de la liste qui contient la reponse de l'utilisateur
                    reponse = reponse[:-1]
                #si on appuie sur 'entrer'
                elif event.key == pygame.K_RETURN:
                    #on teste si la reponse en minuscule est égale a la saisie de l'utilisateur en minuscule
                    if reponse.lower() == reponses[question_index].lower():
                        #si c'est le cas, la variable etat_reponse devient bonne reponse
                        etat_reponse = "Bonne réponse"
                    else:
                        #Sinon elle devient mauvaise reponse
                        etat_reponse = "Mauvaise réponse"
                    # Réinitialiser la réponse
                    reponse = ""
                #si l'entrée de l'utilisateur contient quelque chose
                elif event.unicode != '':
                    #on l'ajoute a la variable reponse
                    reponse += event.unicode
    #on rafraichit la couleur du fond pour que les lettres n'apparaissent qu'une seule fois
    fen.fill(couleur_fond)
    #on affiche la question sur l'interface
    fen.blit(texte_question, rect_question.topleft)

    #on definit la police d'ecriture de la reponse, on l'affiche et sa position
    texte_reponse = font.render(reponse, True, (0, 0, 0))
    #on definit le rectangle dans lequel la reponse s'affichera
    rect_reponse = texte_reponse.get_rect(center=(largeur // 2, hauteur // 2 + 30))
    #on affiche la saisie utilisateur
    fen.blit(texte_reponse, rect_reponse.topleft)

    if etat_reponse:
        message_surface = font.render(etat_reponse, True, (0, 255, 0))
        if etat_reponse == "Bonne réponse":
            couleur = (0, 255, 0)
        else:
            couleur = (255, 0, 0)

        message_rect = message_surface.get_rect(center=(largeur // 2, hauteur // 2 + 60))
        fen.blit(message_surface, message_rect.topleft)
        pygame.time.delay(1000)  # Affiche le message pendant une seconde

        # Passez à la question suivante après avoir affiché le message
        etat_reponse = None
        question_index += 1
        if question_index < len(questions):
            texte_question = font.render(questions[question_index], True, (0, 0, 0))
        else:
            print("Toutes les questions sont terminées.")
            continuer = False

    pygame.display.flip()

pygame.quit()
