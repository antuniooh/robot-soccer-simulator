# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import File_Handling_functions as fh
import math as mth

'''
Sx = ((-0.008 * pow(t, 3)) - (0.15 * pow(t, 2)) + 2.5 * t + 1)
Vx = (((-0.024 * pow(t, 2)) - 0.3 * t + 2.5001)
Ax = ((-0.048 * t) - 0.3)

Sy = - ((0.2 * pow(t, 1.5)) + 1.6*t + 1)
Vy = - ((0,3 * pow(t, 0.5)) + 1.6)
Ay = - (0.15 * pow(t, 0.5))
'''


class Equation:
    def __init__(self, field, intercepX=0, intercepY=0 , time=0):
        self.Field = field
        self.X_ball = []
        self.Y_ball = []
        self.T_ball = []
        self.Sy_Robot = []
        self.Sx_Robot = []
        self.InterceptionPointX = intercepX
        self.InterceptionPointY = intercepY
        self.InterceptionTime = time

    def fill_x_and_y_lists(self):
        self.X_ball, self.Y_ball, self.T_ball = fh.create_matrix(self.Field.Ball_txt, 0)

    def calculate_distance(self, x1, y1, x2, y2):
        X = x2 - x1
        Y = y2 - y1

        R = mth.sqrt(pow(X, 2) + pow(Y, 2))

        return R

    def rect_y(self):
        # print("Tempo Bola: %.5f" % self.Field.Interception_Index_Points[0])

        To = 0
        Tf = self.InterceptionTime

        Yo = self.Field.Robot.Y
        Yf = self.InterceptionPointY

        deltaY = Yf - Yo
        deltaX = Tf - To

        m = deltaY / deltaX
        q = Yf - (m * Tf)

        '''print("deltaY = %.5f  deltaX = %.5f" % (deltaY, deltaX))
        print("m = %.5f  q = %.5f\n" % (m, q))'''

        return m, q

    def rect_x(self):
        print("Tempo Bola: %.5f" % self.Field.Interception_Index_Points[0])

        To = 0
        Tf = self.InterceptionTime

        Xo = self.Field.Robot.X
        Xf = self.InterceptionPointX

        deltaY = Xf - Xo
        deltaX = Tf - To

        m = deltaY / deltaX
        q = Xf - (m * Tf)

        '''print("deltaY = %.5f  deltaX = %.5f" % (deltaY, deltaX))
        print("m = %.5f  q = %.5f\n" % (m, q))'''

        return m, q

    def rect_graphOne(self):
        Xo = self.Field.Robot.X
        Yo = self.Field.Robot.Y
        Xf = self.InterceptionPointX
        Yf = self.InterceptionPointY

        deltaY = Yf - Yo
        deltaX = Xf - Xo

        m = deltaY / deltaX
        q = Yf - m * Xf

        return m, q

    def plot_graph_one(self):

        m, q = self.rect_graphOne()
        x = 0

        Xrobo = []
        Yrobo = []

        Xrobo.append(self.Field.Robot.X)
        Xrobo.append(self.InterceptionPointX)

        Yrobo.append(self.Field.Robot.Y)
        Yrobo.append(self.InterceptionPointY)



        tempX = self.X_ball[0:self.Field.FieldLimit[0]]
        tempY = self.Y_ball[0:self.Field.FieldLimit[0]]
        xB = tempX
        yB = tempY

        plt.plot(Xrobo, Yrobo, color='yellow', label='Trajetória do Robô')
        plt.plot(xB, yB, color='red', label='Trajetória da Bola')

        plt.legend()

        plt.title('Trajetória da Bola e do Robô')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')

        img = mpimg.imread("campo_de_futebol.png")  # imagem de fundo
        plt.imshow(img, extent=[0, 9.5, 0, 6.2])

        InterceptionPoint = self.Field.Interception_Index_Points[0]

        plt.scatter(self.InterceptionPointX, self.InterceptionPointY)
        plt.annotate('Ponto escolhido', xy=(self.InterceptionPointX, self.InterceptionPointY),
                     xytext=(self.InterceptionPointX, self.InterceptionPointY + 1),
                     arrowprops=dict(arrowstyle='->'))

        plt.show()

    def plot_graph_two_Y(self):
        T_ball = []
        Sy_ball = []
        T_robot = []
        Sy_robot = []

        t = 0

        My, Qy = self.rect_y()

        while t <= 4.2:
            SyB = ((0.2 * pow(t, 1.5)) + 1.6 * t + 1)
            SyR = My * t + Qy

            T_ball.append(t)
            Sy_ball.append(SyB)

            T_robot.append(t)
            Sy_robot.append(SyR)

            t += 0.02

        self.Sy_Robot = Sy_robot

        plt.plot(T_ball, Sy_ball, color='red', label='Sy(t) da Bola')
        plt.plot(T_robot, Sy_robot, color='yellow', label='Sy(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Sy da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("S (m)")

        plt.show()

    def plot_graph_two_X(self):
        T_ball = []
        Sx_ball = []
        T_robot = []
        Sx_robot = []

        t = 0

        Mx, Qx = self.rect_x()

        while t <= 4.2:
            VxB = ((-0.008 * pow(t, 3)) - (0.15 * pow(t, 2)) + 2.5 * t + 1)
            VxR = Mx * t + Qx

            T_ball.append(t)
            Sx_ball.append(VxB)

            T_robot.append(t)
            Sx_robot.append(VxR)

            t += 0.02

        self.Sx_Robot = Sx_robot

        plt.plot(T_ball, Sx_ball, color='red', label='Sy(t) da Bola')
        plt.plot(T_robot, Sx_robot, color='yellow', label='Sy(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Sx da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("S (m)")

        plt.show()

    def plot_graph_threeY(self):
        T_ball = []
        Vy_ball = []
        T_robot = []
        Vy_robot = []

        t = 0

        My, Qy = self.rect_y()

        while t <= 4.2:
            VyB = ((-0.024 * pow(t, 2)) - 0.3 * t + 2.5)
            VyR = My
            T_ball.append(t)
            Vy_ball.append(VyB)

            T_robot.append(t)
            Vy_robot.append(VyR)

            t += 0.02

        plt.plot(T_ball, Vy_ball, color='red', label='Vy(t) da Bola')
        plt.plot(T_robot, Vy_robot, color='yellow', label='Vy(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Vy da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("v (m/s)")

        plt.show()

    def plot_graph_threeX(self):
        T_ball = []
        Vx_ball = []
        T_robot = []
        Vx_robot = []

        t = 0

        Mx, Qx = self.rect_x()

        while t <= 4.2:
            VxB = -1 * 0.3 * pow(t, 0.5) + 1.6
            VxR = Mx
            T_ball.append(t)
            Vx_ball.append(VxB)

            T_robot.append(t)
            Vx_robot.append(VxR)

            t += 0.02

        plt.plot(T_ball, Vx_ball, color='red', label='Vx(t) da Bola')
        plt.plot(T_robot, Vx_robot, color='yellow', label='Vx(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Vx da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("v (m/s)")

        plt.show()

    def plot_graph_fourY(self):
        T_ball = []
        Ay_ball = []
        T_robot = []
        Ay_robot = []

        t = 0

        while t <= 4.2:
            AyB = -1 * (0.15 * pow(t, 0.5))
            AyR = 0
            T_ball.append(t)
            Ay_ball.append(AyB)

            T_robot.append(t)
            Ay_robot.append(AyR)

            t += 0.02

        plt.plot(T_ball, Ay_ball, color='red', label='Ay(t) da Bola')
        plt.plot(T_robot, Ay_robot, color='yellow', label='Ay(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Ay da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("A (m/s²)")

        plt.show()

    def plot_graph_fourX(self):
        T_ball = []
        Ax_ball = []
        T_robot = []
        Ax_robot = []

        t = 0

        while t <= 4.2:
            AxB = ((-0.048 * t) - 0.3)
            AxR = 0
            T_ball.append(t)
            Ax_ball.append(AxB)

            T_robot.append(t)
            Ax_robot.append(AxR)

            t += 0.02

        plt.plot(T_ball, Ax_ball, color='red', label='Ax(t) da Bola')
        plt.plot(T_robot, Ax_robot, color='yellow', label='Ax(t) do Robô')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da componente Ax da Bola e do Robô")
        plt.xlabel("t (s)")
        plt.ylabel("A (m/s²)")

        plt.show()

    def plot_graph_five(self):
        distances = []
        time = []

        Sy_Robot = []
        Sx_Robot = []

        index = 0

        t = 0

        My, Qy = self.rect_y()
        Mx, Qx = self.rect_x()

        while t <= 4.2:
            SyR = My * t + Qy
            SxR = Mx * t + Qx

            Sy_Robot.append(SyR)
            Sx_Robot.append(SxR)

            t += 0.02

        t = 0

        xrobot = 0
        yrobot = 0

        while xrobot != self.InterceptionPointX and yrobot != self.InterceptionPointY:
            xball = self.X_ball[index]
            yball = self.Y_ball[index]
            xrobot = Sx_Robot[index]
            yrobot = Sy_Robot[index]

            distance = self.calculate_distance(xball, yball, xrobot, yrobot)
            #print("d = %.3f  R(%.3f, %.3f) B(%.3f, %.3f)" % (distance, xrobot, yrobot, xball, yball))
            distances.append(distance)

            time.append(t)

            index += 1
            t += 0.02

        plt.plot(time, distances, color='red', label='Distância relativa do Robô à Bola')

        plt.axis('equal')

        plt.legend()
        plt.grid(True)

        plt.title("Gráfico da distância relativa entre Robô e a Bola em função do tempo")
        plt.xlabel("t (s)")
        plt.ylabel("d (m)")

        plt.show()
