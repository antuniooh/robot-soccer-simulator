import BP_classes as bpc
import BP_graphs as bpg


def get_robot_x():
    X_robot = float(input("X: "))
    X_robot = float(X_robot)

    return float(X_robot)


def get_robot_y():
    Y_robot = float(input("Y: "))
    Y_robot = float(Y_robot)

    return Y_robot


def create_robot():
    x = get_robot_x()
    y = get_robot_y()

    Robot = bpc.Robot(x, y)

    return Robot


def create_ball():
    Ball = bpc.Ball()

    return Ball


def create_field(ball, robot, coordinates):
    Field = bpc.Field(ball, robot, coordinates)

    return Field


def get_interception_points(field):
    if len(field.Interception_Index_Points) > 0:
        print("QUANTIDADE DE PONTOS POSSIVEIS: " + str(len(field.Interception_Index_Points)))
        print("-------------------------------------------------------------------------------------")

        for line in range(len(field.Interception_Index_Points)):
            print("PONTOS POSSIVEIS DE INTERCEPTAÇÃO:"
                  " X:" + str(field.Ball_txt[field.Interception_Index_Points[line]][1])
                  + " Y:" + str(field.Ball_txt[field.Interception_Index_Points[line]][2]))
            print("TEMPO QUE O ROBO LEVA PARA CHEGAR:  %.3fs  Bola: %ss" %
                  (field.Interception_Robot[line][0], str(field.Ball_txt[field.Interception_Index_Points[line]][0])))
            print("-------------------------------------------------------------------------------------")

    else:
        print("O robô NÃO intercepta a bola")


def plot_graph_one(field):
    pass


def print_ball(ball):
    print("Bola.x = %.3f   Bola.y = %.3f   Bola.time = %.2f" % (ball.X_ball, ball.Y_ball, ball.T_ball), end=' ')
