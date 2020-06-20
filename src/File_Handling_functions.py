def my_float(float_string):
    float_string = str(float_string)
    errormsg = "ValueError: Input must be decimal or integer string"
    try:
        if float_string.count(".") == 1 and float_string.count(",") == 0:
            return float(float_string)
        else:
            middle_string = list(float_string)
            while middle_string.count(".") != 0:
                middle_string.remove(".")
            out_string = str.replace("".join(middle_string), ",", ".")
        return float(out_string)
    except ValueError as error:
        print("%s\n%s" % (errormsg, error))
        return None


def read_file(name):
    file = open("bola.txt", 'r')

    coordinates = []

    i = 0
    for line in file.readlines():
        if i != 0:
            line = line.strip().split('\t')
            line[0] = my_float(line[0])
            line[1] = my_float(line[1])
            line[2] = my_float(line[2])
            if float(line[1]) <= 9 and float(line[2]) <= 6:
                coordinates.append(line)
            if float(line[1]) > 9 or float(line[2]) > 6:
                break
        else:
            i += 1

    file.close()

    return coordinates


def create_matrix(coordinates, type=0):
    X_ball = []
    Y_ball = []
    T_ball = []
    for line in range(len(coordinates)):
        T_ball.append(float(coordinates[line][0]))
        X_ball.append(float(coordinates[line][1]))
        Y_ball.append(float(coordinates[line][2]))

    if type == 0:
        return X_ball, Y_ball, T_ball
    else:
        return X_ball, Y_ball
