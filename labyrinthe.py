__author__ = 'Tanguy,Romain,William'

from tkinter import Canvas

class Labyrinthe:
    def __init__(self, nbe_colonne, nbe_ligne, fenetre_parent):
        """
        Constructeur
        :param nbe_colonne: représente le nombre de colonne qu'aura la grille
        :param nbe_ligne: représente le nombre de ligne qu'aura la grille
        :return:
        """
        # On créé la grille selon le nbe de colonne et ligne spécifié
        self.grille = []
        for i in range(nbe_colonne):
            self.grille.append([])
            for j in range(nbe_ligne):
                self.grille[i].append('mur')
        # On crée un canvas qui représentera graphiquement le labyrinthe
        self.laby = Canvas(fenetre_parent, width='800', height='800')
        self.largeur_carre = 40  # Largeur du carré
        self.hauteur_carre = 40  # hauteur du carré
        # Coordonnées du coin haut gauche de la grille
        orig_x = 2
        orig_y = 2
        # On dessine tout
        for i in range(len(self.grille)):
            for j in range(len(self.grille)):
                pos_x = i * self.largeur_carre + orig_x
                pos_y = j * self.hauteur_carre + orig_y
                width = (i + 1) * self.largeur_carre + orig_x
                height = (j + 1) * self.hauteur_carre + orig_y
                tag = ("{}".format(i), "{}".format(j))
                self.laby.create_rectangle(pos_x, pos_y, width, height, fill='green', outline='blue', tags=tag)

    def afficher_grille(self):
        """
        Affiche toutes les valeurs de la grille via la sortie standard
        :return:
        """
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                print(self.grille[i][j])
