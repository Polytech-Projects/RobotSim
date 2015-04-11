#!/usr/bin/python

__author__ = 'Tanguy,Romain,William,Denis'

""" Importation des packages """
from tkinter import *

""" Définition des fonctions """
def init():
    FenetrePrincipale.title("Simulation déplacement d'un robot")
    Graphique.config(width=800, height=600, bg='white')
    Graphique.pack()


""" Fonction permettant de simplifier la création d'un tableau
    """
def creation_tableau(x, y):
    tab = []
    for i in range(x):
        tab.append([])
        for j in range(y):
            tab[i].append(0)
    return tab


""" Fonctin permettant d'afficher les valeur de chaque case de la grille
    l'une à la suite de l'autre
    """
def afficher_grille():
    for i in range(len(Grille)):
        for j in range(len(Grille[i])):
            print(Grille[i][j])


""" Fonction permettant d'afficher les valeurs de la grilles via la console
    """
def afficher_grille_console():
    for i in range(len(Grille)):
        print(Grille[i])


""" Fonction permettant de dessiner la grille du labyrinthe
    dans le canevas donné
    """
def dessiner_grille(canevas):
    width = 40  # Largeur du carré
    height = 40  # hauteur du carré
    """ Coordonnées du coin haut gauche de la grille
        """
    orig_x = 2
    orig_y = 2
    # create_line(x, y, vx, vy, fill='color')
    # create_rectangle(x, y, width, height, fill='blue')
    # On supprime tout le dessin
    canevas.delete(ALL)
    # On redessine tout
    for i in range(len(Grille)):
        for j in range(len(Grille)):
            pos_x = i * width + orig_x
            pos_y = j * height + orig_y
            width_bis = (i + 1) * width + orig_x
            height_bis = (j + 1) * height + orig_y
            r_tag = ("{}".format(i), "{}".format(j))
            canevas.create_rectangle(pos_x, pos_y, width_bis, height_bis, fill='green', outline='blue', tags=r_tag)


""" Définition des variables """
FenetrePrincipale = Tk()
Graphique = Canvas(FenetrePrincipale)
Grille = creation_tableau(10, 20)
dessiner_grille(Graphique)

# Initialisation
init()

# Lancement du programme
FenetrePrincipale.mainloop()
