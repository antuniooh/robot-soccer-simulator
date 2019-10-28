import math as m


class Robot:
    def __init__(self, x, y, radius=0.279, speed=0.4):
        self.X = x
        self.Y = y
        self.Radius = radius
        self.Speed = speed


class Ball:
    def __init__(self, x=0, y=0, time=0, radius=0.11):
        self.X = x
        self.Y = y
        self.Time = time
        self.Radius = radius


class Field:
    def __init__(self, ball, robot, ball_txt, ball_in_game_time=4.2):
        self.Ball = ball
        self.Robot = robot
        self.Ball_txt = ball_txt
        self.In_game_time = ball_in_game_time
        self.Interception_Index_Points = []
        self.Interception_Robot = [[0, robot.X, robot.Y]]

    def calculate_distance(self, robot, ball):
        x = robot.X - ball.X
        y = robot.Y - ball.Y

        result = m.sqrt(pow(x, 2) + pow(y, 2))

        result -= (robot.Radius + ball.Radius)

        return result

    def append_lists(self, index):
        robot = self.Robot
        ball = Ball()
        ball.X = self.Ball.X
        ball.Y = self.Ball.Y
        ball.Time = self.Ball.Time

        distance = self.calculate_distance(robot, ball)

        time = distance/self.Robot.Speed

        if time <= ball.Time and time <= self.In_game_time:
            if distance <= 0:
                time = 0
            self.Interception_Index_Points.append(index)
            self.Interception_Robot.append([time, ball.X, ball.Y])

    def run_coordinates(self):
        i = 0
        for line in self.Ball_txt:
            self.Ball.X = float(line[1])
            self.Ball.Y = float(line[2])
            self.Ball.Time = float(line[0])
            self.append_lists(i)
            i += 1
