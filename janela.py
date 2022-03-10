from tkinter import *

#Cores
azul= '#1a9ab0'

#Cria a janela
janela = Tk()
janela.title('Olá Mundo')
janela.geometry('600x250')
janela.config(bg=azul)

#Adiciona uma foto
janela.iconphoto(False, PhotoImage(file='naruto_1.png'))

#Bloqueia a largura
janela.resizable(width=False, height=True)

janela.mainloop()