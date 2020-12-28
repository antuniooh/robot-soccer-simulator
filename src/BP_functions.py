# -*- coding: utf-8 -*-

import BP_classes as bpc
import BP_graphs as bpg
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import *

MPontos = []

def get_robot_x():
    X_robot = float(input("X: "))
    X_robot = float(X_robot)

    return float(X_robot)

def get_robot_y():
    Y_robot = float(input("Y: "))
    Y_robot = float(Y_robot)

    return Y_robot


def create_robot(x, y):
    Robot = bpc.Robot(x, y)

    return Robot


def create_ball():
    Ball = bpc.Ball()

    return Ball


def create_field(ball, robot, coordinates):
    Field = bpc.Field(ball, robot, coordinates)

    return Field


def get_interception_points(field, mostraPontos):

    if len(field.Interception_Index_Points) > 0:
        mostraPontos.insert(END, "")
        mostraPontos.insert(END,
                            ("                                        QUANTIDADE DE PONTOS POSSIVEIS: " + str(len(field.Interception_Index_Points))))
        mostraPontos.insert(END, "")
        mostraPontos.insert(END, "----------------------------------------------------------------------------------------------------------------------------------------------------")

        for line in range(len(field.Interception_Index_Points)):
            a=[]
            mostraPontos.insert(END, "                          PONTOS POSSIVEIS DE INTERCEPTAÇÃO:"
                                     " X:" + str(field.Ball_txt[field.Interception_Index_Points[line]][1])
                                + " Y:" + str(field.Ball_txt[field.Interception_Index_Points[line]][2]))
            mostraPontos.insert(END, "                      TEMPO QUE O ROBO LEVA PARA CHEGAR:  %.3fs  Bola: %ss" %
                                (field.Interception_Robot[line][0],
                                 str(field.Ball_txt[field.Interception_Index_Points[line]][0])))
            mostraPontos.insert(END, "------------------------------------------------------------------------------------------------------------------------------------------------")
            a.append(field.Ball_txt[field.Interception_Index_Points[line]][0])
            a.append(field.Ball_txt[field.Interception_Index_Points[line]][1])
            a.append(field.Ball_txt[field.Interception_Index_Points[line]][2])
            MPontos.append(a)
        #print(MPontos[0])
        return 1
    else:
        return 0


def plot_graph_one(field):
    pass


def print_ball(ball):
    print("Bola.x = %.3f   Bola.y = %.3f   Bola.time = %.2f" % (ball.X_ball, ball.Y_ball, ball.T_ball), end=' ')
