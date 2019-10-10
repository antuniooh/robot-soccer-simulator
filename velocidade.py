from math import sqrt #importar a biblioteca

#y = -0,008x3 - 0,15x2 + 2,5x + 1: equação da x(t)
# derivada = -0,24x^2 - 0,30x +2,5

for j in range(len(coordenadas)):
    VxBola = []
    #calculo da velocidade instantanea
    v = -0.24*((coordenadas[j][0])**2) - 0.30*(coordenadas[j][0]) + 2.5
    VxBola.append(v)
