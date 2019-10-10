from math import sqrt #importar a biblioteca
from graficos import * #importar as funções de gráfico


arquivo = open('bola.txt','r+') #ler aquivo de texto
coordenadas =[]

#adicionar na matriz de coordenadas X,Y e tempo
for linha in arquivo.readlines():
    a = linha.strip() #quebra o fim de linha
    a = linha.split('\t') #divide nos tabs
    coordenadas.append(a) #adiciona na matriz
arquivo.close() #fecha o arquivo

#matrizes separadas para a representaÃ§Ã£o grafica da bola
Xbola=[]
Ybola=[]
Tbola= []
for j in range(len(coordenadas)):
    Tbola.append(float(coordenadas[j][0]))
    Xbola.append(float(coordenadas[j][1]))
    Ybola.append(float(coordenadas[j][2]))

# entrada de coordenadas do robo, caso em que o robo estÃ¡ fora do campo
x = float(input("Digite o X inicial do robo: "))
y = float(input("Digite o Y inicial do robo: "))
while x > 9 or y > 6:
    print('ESCREVE DIREITO CORNO')
    x = float(input("Digite o X inicial do robo: "))
    y = float(input("Digite o Y inicial do robo: "))


PPI =[] #vetor de pontos possiveis de interceptaÃ§Ã£o
TRI =[] #vetor de tempos possiveis de interceptaÃ§Ã£o
TM = 4.2 #variavel de tempo máximo, pois fora disso a bola está fora do campo

#for para saber todas as distancias
for i in range(len(coordenadas)):
    raioBola = 0.11 #raio padrão de bola da copa em mettros
    raioRobo = 0.3945 #raio do robô (tamanho da perna) em metros
    VelRobo = 0.40 # m/s - humanoide

    #distancia entre o ponto inicial do robo e todas as coordenadas da bola, entre os centros
    dist = (sqrt(((x - float(coordenadas[i][1]))**2) + ((y - float(coordenadas[i][2]))**2)))
    dist -= raioBola + raioRobo


    T = 0
    if dist <= 0:
        PI = i # o indice do ponto
        PPI.append(PI) #adiciona o indice do ponto de interceptaÃ§Ã£o
        TRI.append(T) #adiciona o tempo do robo como sendo 0, pois os raios estão interceptando
    else:
        #calcular se o robo chega antes da bola em algum ponto
        T = (dist)/VelRobo #tempo que o robo leva para chegar ao ponto da bola

        #caso ele chegue antes/ao mesmo tempo q a bola no ponto, significa que Ã© possivel intercepta-la
        if T <= float(coordenadas[i][0]):
            if T <= TM: #caso o tempo seja menor que o maximo
                TM = T #o tempo máximo passa a ser o T
                PI = i # o indice do ponto ideal passa a ser esse

            PPI.append(PI) #adiciona o indice do ponto de interceptaÃ§Ã£o
            TRI.append(T) #adiciona o tempo do robo
            #objetivo é achar, além de todos os pontos possiveis, o ideal (mais próximo)

        else:
            pass


#caso a lista de pontos de inetrceptção esteja vazia
if len(PPI) == 0:
    print("NÃ£o hÃ¡ pontos possiveis de interceptaÃ§Ã£o")
else:
    print("QUANTIDADE DE PONTOS POSSIVEIS: " + str(len(PPI)))
    print("-------------------------------------------------------------------------------------")
    for k in PPI:
        indice = 0
        #exibe todos os pontos possiveis de inetreceptação, além do tempo que o orobo leva para chegar lá
        print("PONTOS POSSIVEIS DE INTERCEPTAÃ‡Ã‚O: X:"+str(coordenadas[k][1]) + " Y:"+str(coordenadas[k][2]))
        print("TEMPO QUE O ROBO LEVA PARA CHEGAR: "+ str(TRI[indice]) + "s  Bola: "+str(coordenadas[k][0]))
        print("-------------------------------------------------------------------------------------")
        indice+= 1

    #chamar as funções de gráfico caso haja pontos de interceptação
    #grafico1(coordenadas,Xbola,Ybola,x,y,PPI,PI)
    #grafico2(coordenadas,Xbola,Ybola,x,y,PPI,PI)
    #grafico3(coordenadas,Xbola,Ybola,x,y,PPI,PI)
    #grafico4(coordenadas,Xbola,Ybola,x,y,PPI,PI)
    #grafico5(coordenadas,Xbola,Ybola,x,y,PPI,PI)



