from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import string
import random

#Lista de cores
cor0 = '#444466' #Black
cor1 = '#feffff' #White
cor2 = '#f05a43' #Red

janela = Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor1)
estilo = ttk.Style(janela)
estilo.theme_use('clam')


#Frame Superior
frame_superior = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_superior.grid(row=0, column=0, sticky=NSEW)
image = Image.open('cadeado_01.png')
image = image.resize((40, 30), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
logo = Label(frame_superior, height=60, image=image, compound=LEFT, padx=10, relief='flat', anchor=NW, bg=cor1)
logo.place(x=2, y=0)

logo_nome = Label(frame_superior, text='Gerador de Senhas', width=20, height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 16 bold'), bg=cor1, fg=cor0)
logo_nome.place(x=40, y=2)

logo_linha = Label(frame_superior, width=295, height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor0)
logo_linha.place(x=0, y=35)


#Parte lógica do código
def criar_senha():
    caracter_maiusculo = string.ascii_uppercase
    caracter_minusculo = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '!@#$%&*,.'
    
    global combinar
    combinar = ''
    if estado_1.get() == caracter_maiusculo:
       combinar = caracter_maiusculo
    else:
        pass
    if estado_2.get() == caracter_minusculo:
       combinar = combinar + caracter_minusculo
    else:
        pass
        
    if estado_3.get() == numeros:
       combinar = combinar + numeros
    else:
        pass

    if estado_4.get() == simbolos:
       combinar = combinar + simbolos
    else:
        pass

    comprimento = int(caixa.get())
    senha = "".join(random.sample(combinar, comprimento))

    exibe_senha['text'] = senha

    def copiar_senha():
        copiar = senha
        frame_inferior.clipboard_clear()
        frame_inferior.clipboard_append(copiar)

        messagebox.showinfo('sucesso', 'A senha foi copiada com sucesso!')
        
    btn_copiar_senha = Button(frame_inferior, command=copiar_senha, text='Copiar', width=6, height=2, relief='raised', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
    btn_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)

#Fraime inferior
frame_inferior = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW)

exibe_senha = Label(frame_inferior, text='----', width=21, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor0)
exibe_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

num_caracteres = Label(frame_inferior, text='Número total de caracteres', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
num_caracteres.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(8)
caixa = Spinbox(frame_inferior, from_=0, to=20, width=5, textvariable=var)
caixa.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=1)

caracter_maiusculo = string.ascii_uppercase
caracter_minusculo = string.ascii_lowercase
numeros = '123456789'
simbolos = '!@#$%&*,.'


frame_caracteres = Frame(frame_inferior, width=295, height=210, bg=cor1, pady=0, padx=1, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=2)

#Caracteres letras maiusculas
estado_1 = StringVar()
estado_1.set(False)
caixa_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=caracter_maiusculo, offvalue='off', relief='flat', bg=cor1)
caixa_1.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
num_caracteres = Label(frame_caracteres, text='Letras maiusculas(ABC)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
num_caracteres.grid(row=2, column=1, sticky=NW, padx=0, pady=5)

#Caracteres letras minusculas
estado_2 = StringVar()
estado_2.set(False)
caixa_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=caracter_minusculo, offvalue='off', relief='flat', bg=cor1)
caixa_2.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
num_caracteres = Label(frame_caracteres, text='Letras minusculas(abc)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
num_caracteres.grid(row=3, column=1, sticky=NW, padx=0, pady=5)

#Números
estado_3 = StringVar()
estado_3.set(False)
caixa_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=cor1)
caixa_3.grid(row=4, column=0, sticky=NW, padx=2, pady=5)
num_caracteres = Label(frame_caracteres, text='Números(123)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
num_caracteres.grid(row=4, column=1, sticky=NW, padx=0, pady=5)

#Símbolos
estado_4 = StringVar()
estado_4.set(False)
caixa_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor1)
caixa_4.grid(row=5, column=0, sticky=NW, padx=2, pady=5)
num_caracteres = Label(frame_caracteres, text='Símbolos(#&*)', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
num_caracteres.grid(row=5, column=1, sticky=NW, padx=0, pady=5)

#Botão gerador das senhas
btn_gerador_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha', width=34, height=1, relief='flat', overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor1)
btn_gerador_senha.grid(row=6, column=0, sticky=NSEW, padx=5, pady=20, columnspan=5)





janela.mainloop()
