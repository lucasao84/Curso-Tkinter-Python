from tkinter import *

#Configurando janela

janela = Tk()
janela.title("Frame")
janela.geometry('408x400')

#Criando Frame

frame_nav = Frame(janela, width=400, height=20, bg="white")
frame_nav.grid(row=0, column=0,columnspan=3, padx=0, pady=2)

frame_esquerda= Frame(janela, width=100, height=200, bg="#F0F2F5")
frame_esquerda.grid(row=1, column=0,padx=2)

frame_meio = Frame(janela, width=200, height=200, bg="white")
frame_meio.grid(row=1, column=1)

frame_direita = Frame(janela, width=100, height=200, bg="#F0F2F5")
frame_direita.grid(row=1, column=2, padx=2)





janela.mainloop()


