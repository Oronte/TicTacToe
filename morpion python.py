
'''lancer la fonction morpion() dans la console pour lancer le jeu'''

def afficher_grille(grille):    #affiche la grille en mettant des lignes et des cases correspondant au nombres de cases jouable
    for ligne in grille:
        for case in ligne:
            print(case, end='|')
        print('')

def demander_position():       #demande au joueur la ligne et la colonne
    ligne = int(input("Choisis une ligne (1, 2 ou 3) : ")) - 1
    colonne = int(input("Choisis une colonne (1, 2 ou 3) : ")) - 1
    return ligne, colonne

def placer_symbole(grille, joueur, ligne, colonne):     #regarde la case est occupée et sinon place le signe du joueur danns la case
    if grille[ligne][colonne] != ' ':
        print("case occupée,choisis une autre case.")
        return False
    else:
        grille[ligne][colonne] = joueur
        return True

def verifier_victoire(grille, joueur):       #regarde si le joueur a gagné en regardant toute les possibilités gagnante
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == joueur:
            return True
        if grille[0][i] == grille[1][i] == grille[2][i] == joueur:
            return True
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False

def verifier_match_nul(grille):        #regarde si il y a une case vide sinon match nul
    for ligne in grille:
        for case in ligne:
            if case == ' ':
                return False
    return True

def morpion():
    grille = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]     #le nombre de ligne et de colonne de la grille
    joueur = 'X'

    while True:
        afficher_grille(grille)
        ligne, colonne = demander_position()
        if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:       #regarde si la ligne/la colonne entré est possible sinon message d'erreur et interromp le reste du block
            print("Position pas possible, choisis une case valide.")
            continue
        if not placer_symbole(grille, joueur, ligne, colonne):         #regarde si la fonction placer_symbole marche sinon interromp le reste du block
            continue
        if verifier_victoire(grille, joueur):                          #si quelqun a gagner affiche le signe du joueur
            print("Le joueur", joueur, "a gagné !")
            return
        if verifier_match_nul(grille):                                 #si match nul affiche match nul
            print("Match nul !")
            return
        if joueur == 'X':                                              #pour changer de personne a chque tour: si le joueur X a joué c'est au joueur O sinon c'est au joueur X
            joueur = 'O'
        else:
            joueur = 'X'



