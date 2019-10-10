import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# pip install matplotlib

#Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação;
def grafico1(coordenadas, xbola, ybola,Xi, Yi,vetor,PontoIdeal):
    for l in vetor:
        X=[Xi, float(coordenadas[l][1])]
        Y =[Yi, float(coordenadas[l][2])]
        plt.plot(X, Y, 's')
        plt.plot(xbola, ybola,'k--', color='red')
        plt.plot(X, Y, color ='blue')

    p = len(vetor)
    plt.title(str(p) +' Pontos PossÃ­veis de InterceptaÃ§Ã£o')
    plt.xlabel('x/s')
    plt.ylabel('y/s')

    img = mpimg.imread("naruto.png") #imagem de fundo
    plt.imshow(img,extent=[0, 9.5, 0, 6.2])

    plt.scatter(float(coordenadas[PontoIdeal][1]),float(coordenadas[PontoIdeal][2]))
    plt.annotate('Ponto com Menor Tempo', xy=(float(coordenadas[PontoIdeal][1]),float(coordenadas[PontoIdeal][2])), xytext=(float(coordenadas[PontoIdeal][1]) +1,float(coordenadas[PontoIdeal][2])+1),
                arrowprops=dict(arrowstyle='->'))

    plt.show()

#Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação;
def grafico2(xbola, ybola, tbola, Xi, Yi,PontoIdeal):
    XB=[xbola[0], xbola[PontoIdeal]]
    YB=[xbola[0], xbola[PontoIdeal]]
    TB =[tbola[0], tbola[PontoIdeal]]

    plt.plot(XB, TB, 's')
    plt.plot(YB, TB,'k--', color='red')
    plt.ylabel('y/s')

    #img = mpimg.imread("naruto.png") #imagem de fundo
    #plt.imshow(img,extent=[0, 9.5, 0, 6.2])

    plt.show()

#Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡 até o instante de interceptação;
def grafico3(xbola, ybola, tbola, Xi, Yi,PontoIdeal):
    XB=[xbola[0], xbola[PontoIdeal]]
    YB=[xbola[0], xbola[PontoIdeal]]
    TB =[tbola[0], tbola[PontoIdeal]]

    plt.plot(XB, TB, 's')
    plt.plot(YB, TB,'k--', color='red')
    plt.ylabel('y/s')

    #img = mpimg.imread("naruto.png") #imagem de fundo
    #plt.imshow(img,extent=[0, 9.5, 0, 6.2])

    plt.show()

#Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡 até o instante de interceptação;
def grafico4(xbola, ybola, tbola, Xi, Yi,PontoIdeal):
    XB=[xbola[0], xbola[PontoIdeal]]
    YB=[xbola[0], xbola[PontoIdeal]]
    TB =[tbola[0], tbola[PontoIdeal]]

    plt.plot(XB, TB, 's')
    plt.plot(YB, TB,'k--', color='red')
    plt.ylabel('y/s')

    #img = mpimg.imread("naruto.png") #imagem de fundo
    #plt.imshow(img,extent=[0, 9.5, 0, 6.2])

    plt.show()

#Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡 até o instante de interceptação
def grafico5(xbola, ybola, tbola, Xi, Yi,PontoIdeal):
    XB=[xbola[0], xbola[PontoIdeal]]
    YB=[xbola[0], xbola[PontoIdeal]]
    TB =[tbola[0], tbola[PontoIdeal]]

    plt.plot(XB, TB, 's')
    plt.plot(YB, TB,'k--', color='red')
    plt.ylabel('y/s')

    #img = mpimg.imread("naruto.png") #imagem de fundo
    #plt.imshow(img,extent=[0, 9.5, 0, 6.2])

    plt.show()