# -*- coding: utf-8 -*-

__author__ = 'Tanguy,Romain,William'

from tkinter import Canvas


class Labyrinthe():
    def __init__(self, fenetre_parent):
        """
        Constructeur
        :return:
        """

        """ Définitions des variables """
        self.grille = []
        self.robot_start_x = 0
        self.robot_start_y = 0
        self.lire_fichier('laby.txt')
        self.largeur_carre = 40  # Largeur du carré
        self.hauteur_carre = 40  # hauteur du carré

        # On crée un canvas qui représentera graphiquement le labyrinthe
        width_canvas = "{}".format(self.largeur_carre * len(self.grille[0]))
        height_canvas = "{}".format(self.hauteur_carre * len(self.grille))
        self.laby = Canvas(fenetre_parent, width=width_canvas, height=height_canvas)
        # Coordonnées du coin haut gauche de la grille
        orig_x = 2
        orig_y = 2
        # On dessine tout
        for i in range(len(self.grille[0])):
            for j in range(len(self.grille)):
                pos_x = i * self.largeur_carre + orig_x
                pos_y = j * self.hauteur_carre + orig_y
                width = (i + 1) * self.largeur_carre + orig_x
                height = (j + 1) * self.hauteur_carre + orig_y
                tag = ("{}".format(i), "{}".format(j))
                color = ''
                if self.grille[j][i] == 'mur':
                    color = 'black'
                if self.grille[j][i] == 'vide':
                    color = 'white'
                self.laby.create_rectangle(pos_x, pos_y, width, height, fill=color, outline='blue', tags=tag)
        self.laby.pack()

    def afficher_grille(self):
        """
        Affiche toutes les valeurs de la grille via la sortie standard
        :return:
        """
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                print(self.grille[i][j])

    def afficher_tableau(self):
        for i in range(len(self.grille)):
            print(self.grille[i])

    def lire_fichier(self, filename):
        file = open(filename, 'r')
        i = 0
        for ligne in file:
            self.grille.append([])
            for j in range(len(ligne)):
                if ligne[j] == 'X':
                    self.grille[i].append('mur')
                if ligne[j] == 'O':
                    self.grille[i].append('vide')
                if ligne[j] == 'E':
                    self.grille[i].append('vide')
                    self.robot_start_x = int("{}".format(j))
                    self.robot_start_y = int("{}".format(i))
            i += 1
        print('Lecture du fichier terminé')
        print("Position de départ du robot: [{}][{}]".format(self.robot_start_x, self.robot_start_y))

    def test_case_vide(self, x, y):
        print("x= {}, y= {}".format(x, y))
        print(self.grille[x][y])
        # self.grille[x][y] = 'testé'
        self.afficher_tableau()
        if self.grille[x][y] == 'vide' or self.grille[x][y] == 'testé':
            print('Case vide')
            return True
        else:
            print('Case pleine')
            return False