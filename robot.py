# -*- coding: utf-8 -*-

__author__ = 'Tanguy,Romain,William'

from tkinter import PhotoImage
import time


class Robot():
    """Documentation du robot
    image: stocke l'image du robot (doit etre de type .gif)
    coord_.: contient les coordonnées actuels du robot
    """

    def __init__(self, labyrinthe):
        # ------------ Coordonnées sur écran ------------
        self.coord_x = labyrinthe.robot_start_x * labyrinthe.largeur_carre
        self.coord_y = labyrinthe.robot_start_y * labyrinthe.hauteur_carre
        # ------------ Coordonnées logique ------------
        self.logic_coord_x = labyrinthe.robot_start_y
        self.logic_coord_y = labyrinthe.robot_start_x
        # ------------ Chargement des images ------------
        self.image_up = PhotoImage(file="up.gif")
        self.image_down = PhotoImage(file="down.gif")
        self.image_right = PhotoImage(file="right.gif")
        self.image_left = PhotoImage(file="left.gif")
        # ------------ Mise à l'échelle ------------
        self.displayimage_up = self.image_up.subsample(2, 2)
        self.displayimage_down = self.image_down.subsample(2, 2)
        self.displayimage_right = self.image_right.subsample(2, 2)
        self.displayimage_left = self.image_left.subsample(2, 2)
        # ------------ Création de l'image ------------
        self.display = labyrinthe.laby.create_image(self.coord_x, self.coord_y, anchor='nw', image=self.displayimage_up)
        self.ref_labyrinthe = labyrinthe
        # ------------ Variables pour l'animation de déplacement ------------
        self.anim_count = 0
        self.anim = False
        # ------------ Variables pour l'algorithme ------------
        self.direction_actuel = 'Up'
        self.direction_ancienne = ''

    def move(self, direction):
        if direction == 'Left':
            new_coord_x = self.logic_coord_x
            new_coord_y = self.logic_coord_y - 1
        if direction == 'Up':
            new_coord_x = self.logic_coord_x - 1
            new_coord_y = self.logic_coord_y
        if direction == 'Right':
            new_coord_x = self.logic_coord_x
            new_coord_y = self.logic_coord_y + 1
        if direction == 'Down':
            new_coord_x = self.logic_coord_x + 1
            new_coord_y = self.logic_coord_y

        if self.ref_labyrinthe.test_case_vide(new_coord_x, new_coord_y):
            self.logic_coord_x = new_coord_x
            self.logic_coord_y = new_coord_y
            self.coord_x = self.logic_coord_x * self.ref_labyrinthe.largeur_carre
            self.coord_y = self.logic_coord_y * self.ref_labyrinthe.hauteur_carre
            self.animation(direction)

    def animation(self, direction):
        for i in range(1, 11):
            if direction == 'Up':
                self.ref_labyrinthe.laby.itemconfig(self.display, image=self.displayimage_up)
                self.ref_labyrinthe.laby.move(self.display, 0, -4)
            if direction == 'Left':
                self.ref_labyrinthe.laby.itemconfig(self.display, image=self.displayimage_left)
                self.ref_labyrinthe.laby.move(self.display, -4, 0)
            if direction == 'Down':
                self.ref_labyrinthe.laby.itemconfig(self.display, image=self.displayimage_down)
                self.ref_labyrinthe.laby.move(self.display, 0, 4)
            if direction == 'Right':
                self.ref_labyrinthe.laby.itemconfig(self.display, image=self.displayimage_right)
                self.ref_labyrinthe.laby.move(self.display, 4, 0)
            self.ref_labyrinthe.laby.update()
            time.sleep(0.025)
    
    def algo_droite(self):
        """ Fait comme si le robot longeait le mur droit.
            Au départ s'il ne détecte pas de mur proche de lui, il part vers le haut.
            """
        # On choisi une direction de base arbitrairement qui est Up (définit dans le constructeur)
        if direction == 'Left':
            new_coord_x = self.logic_coord_x
            new_coord_y = self.logic_coord_y - 1
        if direction == 'Up':
            new_coord_x = self.logic_coord_x - 1
            new_coord_y = self.logic_coord_y
        if direction == 'Right':
            new_coord_x = self.logic_coord_x
            new_coord_y = self.logic_coord_y + 1
        if direction == 'Down':
            new_coord_x = self.logic_coord_x + 1
            new_coord_y = self.logic_coord_y
        
        # Si la case est vide on avance, sinon on cherche où se trouve le mur
        if self.ref_labyrinthe.test_case_vide(new_coord_x, new_coord_y):
            self.logic_coord_x = new_coord_x
            self.logic_coord_y = new_coord_y
            self.coord_x = self.logic_coord_x * self.ref_labyrinthe.largeur_carre
            self.coord_y = self.logic_coord_y * self.ref_labyrinthe.hauteur_carre
            self.animation(direction)
        else
            
