from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import BP_functions as bpf


'''def pegaPontos():
    x = float(entraX.get())
    y = float(entraY.get())
    #print(x,y)
    if x > 9 or y > 6:
        errou['text'] = "Ponto fora do campo!!!"
    else:
        Robot = bpf.create_robot(x,y)
'''
def a():

    janela = tk.Tk()
    janela.title("Bomba Patch 2020 ATUALIZADO")
    janela.geometry("1200x700")

    image1 = tk.PhotoImage(file="fifabanner.png")
    image1 = image1.subsample(1, 1)
    labelBG = tk.Label(image=image1)
    labelBG.place(x=0,y=0, relwidth=1.0, relheight=1.0)

    errou = Label(janela, text = "", font = ("Arial Bold", 14))
    errou.place(x=850, y=290, anchor = CENTER)

    pedeX = Label(janela, text = "Digite o X inicial do robo: ", font = ("Arial Bold", 14))
    pedeX.place(x=750, y=350, anchor = CENTER)
    pedeX = Label(janela, text = "Digite o Y inicial do robo: ", font = ("Arial Bold", 14))
    pedeX.place(x=750, y=400, anchor = CENTER)

    entraX = Entry(janela, width = 14, font = ("Arial Bold", 14))
    entraX.place(x=940, y=350, anchor = CENTER)
    entraY = Entry(janela, width = 14, font = ("Arial Bold", 14))
    entraY.place(x=940, y=400, anchor = CENTER)

    #botao = Button(janela, text="Enviar", command = pegaPontos)
    #botao.place(x=840, y=450, anchor = CENTER)



    janela.mainloop()