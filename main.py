#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Tanguy,Romain,William'

""" Importation des packages """
from tkinter import *
import labyrinthe
import robot

def event_handler(event):
    # touche = event.char
    touche = event.keysym
    direction = ''
    """
    if touche == 'z':
        # On déplace le robot vers le haut
        print('swag')
        print(Lab.grille[Rob.coord_x][Rob.coord_y - 1])
        if Lab.grille[Rob.coord_x][Rob.coord_y - 1] != 'mur':
            print('yolo')
            for z in xrange(1,10):
                after(10, move_robot, 'z')
    """

    if touche == 'z' or touche == 'Up':
        # On déplace le robot vers le haut
        direction = 'Up'
    if touche == 'q' or touche == 'Left':
        # On déplace le robot vers la gauche
        direction = 'Left'
    if touche == 's' or touche == 'Down':
        # On déplace le robot vers le bas
        direction = 'Down'
    if touche == 'd' or touche == 'Right':
        # On déplace le robot vers la droite
        direction = 'Right'
    Rob.move(direction)


FenetrePrinc = Tk()
FenetrePrinc.title('Simulation robot')
Lab = labyrinthe.Labyrinthe(FenetrePrinc)
Rob = robot.Robot(Lab)

Lab.afficher_tableau()

Lab.laby.focus_set()
Lab.laby.bind('<Key>', event_handler)

# Lancement de la fenêtre principale
FenetrePrinc.mainloop()