from tkinter import *

# Cores

cor1 = '#E5B1B2' # ROSA
cor2 = 'black'   # PRETO

# Criando janela




janela = Tk()                       # Estancia da janela
janela.title("Janela tkinter")      # Titulo da janela tkinter
janela.geometry('600x250')          # Configurar o tamanho da janela
janela.config(bg=cor2)              # Configurando cor de fundo da janela

janela.resizable(width=False, height=False)  # Tornando a janela não rendimensionavel


janela.mainloop()                   # Comando loop para abrir tkinter