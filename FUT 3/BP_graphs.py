import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import File_Handling_functions as fh

'''
Sx = ((-0.008 * pow(t, 3)) - (0.15 * pow(t, 2)) + 2.5 * t + 1)
Vx = (((-0.024 * pow(t, 2)) - 0.3 * t + 2.5001)
Ax = ((-0.048 * t) - 0.3)

Sy = - ((0.2 * pow(t, 1.5)) + 1.6*t + 1)
Vy = - ((0,3 * pow(t, 0.5)) + 1.6)
Ay = - (0.15 * pow(t, 0.5))
'''


class Equation:
    def __init__(self, field):
        self.Field = field
        self.X_ball = []
        self.Y_ball = []
        self.T_ball = []

    def fill_x_and_y_lists(self):
        self.X_ball, self.Y_ball, self.T_ball = fh.create_matrix(self.Field.Ball_txt, 0)

    def rect_y(self):
        print("Tempo Bola: %.5f" % self.Field.Interception_Index_Points[0])

        To = 0
        Tf = self.Field.Ball_txt[self.Field.Interception_Index_Points[0]][0]

        Yo = self.Field.Robot.Y
        Yf = self.Field.Interception_Robot[1][2]

        deltaY = Yf - Yo
        deltaX = Tf - To

        m = deltaY/deltaX
        q = Yf - (m * Tf)

        print("deltaY = %.5f  deltaX = %.5f" % (deltaY, deltaX))
        print("m = %.5f  q = %.5f\n" % (m, q))

        return m, q

    def plot_graph_one(self):

        xR = [self.Field.Interception_Robot[0][1], self.Field.Interception_Robot[1][1]]
        yR = [self.Field.Interception_Robot[0][2], self.Field.Interception_Robot[1][2]]
        tempX = self.X_ball[0:self.Field.Interception_Index_Points[0]]
        tempY = self.Y_ball[0:self.Field.Interception_Index_Points[0]]
        xB = tempX
        yB = tempY

        plt.plot(xR, yR, color='yellow')
        plt.plot(xB, yB, color='red')

        plt.title(str(len(self.Field.Interception_Index_Points)) + ' Pontos Possíveis de Interceptação')
        plt.xlabel('t(s)')
        plt.ylabel('s(m)')

        img = mpimg.imread("campo_de_futebol.png")  # imagem de fundo
        plt.imshow(img, extent=[0, 9.5, 0, 6.2])

        InterceptionPoint = self.Field.Interception_Index_Points[0]

        plt.scatter(float(self.Field.Ball_txt[InterceptionPoint][1]), float(self.Field.Ball_txt[InterceptionPoint][2]))
        plt.annotate('Ponto com Menor Tempo', xy=(float(self.Field.Ball_txt[InterceptionPoint][1]), float(self.Field.Ball_txt[InterceptionPoint][2])),
                     xytext=(float(self.Field.Ball_txt[InterceptionPoint][1]), float(self.Field.Ball_txt[InterceptionPoint][2]) + 1),
                     arrowprops=dict(arrowstyle='->'))

        plt.show()

    def plot_graph_two(self):
        T_ball = []
        Sx_ball = []
        Sy_ball = []
        T_robot = []
        Sx_robot = []
        Sy_robot = []

        t = 0

        My, Qy = self.rect_y()

        while t <= 4.2:
            SxB = ((-0.008 * pow(t, 3)) - (0.15 * pow(t, 2)) + 2.5 * t + 1)
            # SxR = [equação do robô]

            SyB = ((0.2 * pow(t, 1.5)) + 1.6*t + 1)
            SyR = My * t + Qy

            T_ball.append(t)
            Sy_ball.append(SyB)

            T_robot.append(t)
            Sy_robot.append(SyR)

            t += 0.2

        '''m_robot = ((self.Field.Interception_Robot[1][2] - self.Field.Robot.Y)
             / (self.Field.Interception_Robot[1][1] - self.Field.Robot.X))'''

        plt.plot(T_ball, Sy_ball, color='red', label='Sy(t) da Bola')
        plt.plot(T_robot, Sy_robot, color='yellow', label='Sy(t) do Robô')

        plt.legend()

        plt.title("Gráfico das componentes Sx e Sy da Bola e do Robo")
        plt.xlabel("t(s)")
        plt.ylabel("S(m)")

        plt.show()

    def plot_graph_three(self):
        Vy_ball = []
        Vx_ball = []
        Vx_robot = []
        Vy_robot = []
        i = 0

        while i <= 9:
            x = (2*0.0244*i + 0.4324)
            if x <= self.Field.Interception_Robot[1][2]:
                Vy_ball.append(x)
                Vx_ball.append(i)
                Vx_robot.append(i)
                Vy_robot.append(0.4)
                if x == self.Field.Interception_Robot[1][2]:
                    print(x)
            else:
                break
            i += 0.2

        '''m_robot = ((self.Field.Interception_Robot[1][2] - self.Field.Robot.Y)
             / (self.Field.Interception_Robot[1][1] - self.Field.Robot.X))'''

        plt.plot(Vx_ball, Vy_ball, color='red')
        plt.plot(Vx_robot, Vy_robot, color='yellow')

        plt.title("Gráfico das componentes Vx e Vy da Bola e do Robô")
        plt.xlabel("t(s)")
        plt.ylabel("v(m/s)")

        plt.show()

    def plot_graph_four(self):
        Ay_Ball = []
        Ax_Ball = []
        Ax_Robot = []
        Ay_Robot = []

        i = 0

        while i <= 9:
            x = (2 * 0.0244)
            if x <= self.Field.Interception_Robot[1][2]:
                Ay_Ball.append(x)
                Ax_Ball.append(i)
                Ax_Robot.append(i)
                Ay_Robot.append(0)
                if x == self.Field.Interception_Robot[1][2]:
                    print(x)
            else:
                break
            i += 0.2

        plt.plot(Ax_Ball, Ay_Ball, color='red')
        plt.plot(Ax_Robot, Ay_Robot, color='yellow')

        plt.title("Gráfico das componentes Ax e Ay da Bola e do Robô")
        plt.xlabel("t(s)")
        plt.ylabel("a(m/s^2)")

        plt.show()
