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
        self.coord_x = labyrinthe.robot_start_x * labyrinthe.largeur_carre
        self.coord_y = labyrinthe.robot_start_y * labyrinthe.hauteur_carre
        self.logic_coord_x = labyrinthe.robot_start_y
        self.logic_coord_y = labyrinthe.robot_start_x
        self.image = PhotoImage(file="robot.gif")
        self.displayimage = self.image.subsample(2, 2)
        self.display = labyrinthe.laby.create_image(self.coord_x, self.coord_y, anchor='nw', image=self.displayimage)
        self.ref_labyrinthe = labyrinthe
        self.anim_count = 0
        self.anim = False

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
        """
        if self.anim is False and self.anim_count == 0:
            if direction == 'Up':
                self.ref_labyrinthe.laby.move(self.display, 0, -4)
            if direction == 'Left':
                self.ref_labyrinthe.laby.move(self.display, -4, 0)
            if direction == 'Down':
                self.ref_labyrinthe.laby.move(self.display, 0, 4)
            if direction == 'Right':
                self.ref_labyrinthe.laby.move(self.display, 4, 0)
            self.anim = True
            self.anim_count += 1
            self.ref_labyrinthe.laby.after(500, self.animation(direction))
        if self.anim is True and self.anim_count < 10:
            if direction == 'Up':
                self.ref_labyrinthe.laby.move(self.display, 0, -4)
            if direction == 'Left':
                self.ref_labyrinthe.laby.move(self.display, -4, 0)
            if direction == 'Down':
                self.ref_labyrinthe.laby.move(self.display, 0, 4)
            if direction == 'Right':
                self.ref_labyrinthe.laby.move(self.display, 4, 0)
            self.anim_count += 1
            self.ref_labyrinthe.laby.after(500, self.animation(direction))
        else:
            self.anim = False
            self.anim_count = 0 """
        for i in range(1, 11):
            if direction == 'Up':
                self.ref_labyrinthe.laby.move(self.display, 0, -4)
            if direction == 'Left':
                self.ref_labyrinthe.laby.move(self.display, -4, 0)
            if direction == 'Down':
                self.ref_labyrinthe.laby.move(self.display, 0, 4)
            if direction == 'Right':
                self.ref_labyrinthe.laby.move(self.display, 4, 0)
            self.ref_labyrinthe.laby.update()
            time.sleep(0.025)