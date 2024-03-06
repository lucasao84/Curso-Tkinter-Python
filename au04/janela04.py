from tkinter import *

cor1 = '#C2D0BE'  # cinza
cor2 = '#F5C4DA'  # rosa
cor3 = '#FFED26'  # amrelo

# Criando janela

janela = Tk()
janela.title('Butao')
janela.geometry('300x300')

global contador

contador = 0

# Criando Label widget
label = Label(janela, width=15, height=2, text='Texto apresentado', background=cor2, fg='black', font=('Ivy 10'))
label.grid(row=0, column=0, padx=10, pady=10)

# Definindo função executar
def executar():
    global contador

    texto1 = 'será trocado'
    texto2 = 'você trocou '

    if (contador % 2) == 0:
        resultado = texto2 + str(contador)
        # Update the text of the Label widget
        label['text'] = resultado
        label['bg'] = cor3
    
    else:
        resultado = texto1 + str(contador)
        label['text'] = resultado
        label['bg'] = cor2    

    contador += 1

# Criando botão
texto = Button(janela, width=15, height=2, text='Click aqui', background=cor2, fg='black', font=('Ivy 8'), command=executar)
texto.grid(row=0, column=2, padx=10, pady=10)

janela.mainloop()
