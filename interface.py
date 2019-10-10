# importar o thinker
from tkinter import *
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Bomba Patch 2020 ATUALIZADO")
janela.geometry('1200x700')
janela.configure(background="gray")

#cria imagem de fundo
image1 = tk.PhotoImage(file="FIFA 19.png")
image1 = image1.subsample(1, 1)
labelBG = tk.Label(image=image1)
labelBG.place(x=0,y=0, relwidth=1.0, relheight=1.0)

# criar entrada
entrada = Entry(janela, width=14, font=('Arial', 14))
entrada.place(x=200, y=50, anchor=CENTER)

# criar button
#botao = Button(janela, text="Resultado", command=avaliar)
#botao.place(x=200, y=200, anchor=CENTER)

janela.mainloop()