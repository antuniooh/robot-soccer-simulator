import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import File_Handling_functions as fh


class Equation:
    def __init__(self, field):
        self.Field = field
        self.X_ball = []
        self.Y_ball = []

    def fill_x_and_y_lists(self):
        self.X_ball, self.Y_ball = fh.create_matrix(self.Field.Ball_txt, 1)

    def plot_graph_one(self):
        self.fill_x_and_y_lists()

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
