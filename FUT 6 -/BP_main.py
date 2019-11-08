import BP_classes as bpc
import BP_graphs as bpg
import File_Handling_functions as fh
import BP_functions as bpf
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
import tkinter as tk
from tkinter.ttk import *
import BP_classes as bpc
from tkinter import scrolledtext

acessa = []
a = 2
for i in range(100):
    acessa.append(a)
    a += 3

ponto = []


def imprime(evt):
    w = evt.widget
    x = 0
    index = int(w.curselection()[0])

    para = 0
    for i in range(len(acessa)):
        if acessa[i] == index:
            if len(ponto) == 0:
                ponto.append(bpf.MPontos[i][0])
                ponto.append(bpf.MPontos[i][1])
                ponto.append(bpf.MPontos[i][2])
            else:
                ponto[0] = bpf.MPontos[i][0]
                ponto[1] = bpf.MPontos[i][1]
                ponto[2] = bpf.MPontos[i][2]
            para = 1
            break
    if para == 0:
        messagebox.showinfo("Aviso", "Isto não é um ponto de interceptação!!!")
    value = w.get(index)
    # print(bpf.MPontos[0])

    # print('You selected item %d: "%s"' % (index, value))


def main():
    def imprimePontos():

        def exibeValor():
            print(combo.get())
            print(ponto)
            Graph = bpg.Equation(Field, ponto[1], ponto[2], ponto[0])
            Graph.fill_x_and_y_lists()

            if combo.get() == "Ponto de interceptação":
                Graph.plot_graph_one()

            elif combo.get() == "Posição x Tempo":
                Graph.plot_graph_two_Y()
                Graph.plot_graph_two_X()

            elif combo.get() == "Velocidade x Tempo":
                Graph.plot_graph_threeY()
                Graph.plot_graph_threeX()

            elif combo.get() == "Acelereração x Tempo":
                Graph.plot_graph_fourY()
                Graph.plot_graph_fourX()

            elif combo.get() == "Distancia x Tempo":
                Graph.plot_graph_five()

        nova_janela = tk.Tk()
        nova_janela.title("Bomba Patch 2020 ATUALIZADO")
        nova_janela.geometry("1200x700")

        mostraPontos = Listbox(nova_janela, width=80, height=40, font=("Helvetica", 10), highlightthickness=2,
                               selectbackground="red")
        mostraPontos.place(relx=0.7, rely=0.5, anchor=CENTER)
        mostraPontos.delete(1, END)
        mostraPontos.bind('<<ListboxSelect>>', imprime)

        scrollbar = tk.Scrollbar(nova_janela, orient="vertical")
        scrollbar.config(command=mostraPontos.yview)
        scrollbar.pack(side="right", fill="y")
        mostraPontos.config(yscrollcommand=scrollbar.set)

        if bpf.get_interception_points(Field, mostraPontos):
            combo = Combobox(nova_janela, width=30)
            combo['values'] = (
            "Ponto de interceptação", "Posição x Tempo", "Velocidade x Tempo", "Acelereração x Tempo",
            "Distancia x Tempo")
            combo.current(0)  # definimos o valor padrão!
            combo.pack()
            combo.place(x=280, y=300, anchor=CENTER)

            botao = Button(nova_janela, text="Mostrar Gráfico", command=exibeValor)
            botao.pack()
            botao.place(x=280, y=350, anchor=CENTER)

        nova_janela.mainloop()

    def errou():
        messagebox.showinfo("Aviso", "Ponto fora do campo!!!")

    def pegaPontos():
        x = float(entraX.get())
        y = float(entraY.get())
        # print(x,y)
        if x > 9 or y > 6:
            errou()
        else:
            global Robot
            global Field

            Robot = bpf.create_robot(x, y)

            Ball = bpf.create_ball()
            Field = bpf.create_field(Ball, Robot, Coordinates)

            Field.run_coordinates()

            imprimePontos()

    Coordinates = fh.read_file("bola.txt")

    janela = tk.Tk()
    janela.title("Bomba Patch 2020 ATUALIZADO")
    janela.geometry("1200x700")

    image1 = tk.PhotoImage(file="fifabanner.png")
    image1 = image1.subsample(1, 1)
    labelBG = tk.Label(janela, image=image1)
    labelBG.place(x=0, y=0, relwidth=1.0, relheight=1.0)

    pedeX = Label(janela, text="Digite o X inicial do robo: ", font=("Arial Bold", 14))
    pedeX.place(x=750, y=350, anchor=CENTER)
    pedeX = Label(janela, text="Digite o Y inicial do robo: ", font=("Arial Bold", 14))
    pedeX.place(x=750, y=400, anchor=CENTER)

    entraX = Entry(janela, width=14, font=("Arial Bold", 14))
    entraX.place(x=940, y=350, anchor=CENTER)
    entraY = Entry(janela, width=14, font=("Arial Bold", 14))
    entraY.place(x=940, y=400, anchor=CENTER)

    botao = tk.Button(janela, text="Enviar", bd="5", width=8, height=2, command=pegaPontos)
    botao["background"] = "#ccff66"
    botao.pack(side='top')
    botao.place(x=840, y=460, anchor=CENTER)

    janela.mainloop()


if __name__ == "__main__":
    main()
