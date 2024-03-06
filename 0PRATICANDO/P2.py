from tkinter import * 

# cores

cor1 = '#C2D0BE'  # cinza
cor2 = '#F5C4DA'  # rosa
cor3 = '#FFED26'  # amrelo


# criando janela

janela = Tk()
janela.title('PRATICANDO')
janela.geometry('250x250')

global Contador

contador = 0

def execultar():
    global contador
    texto1 = 'trocou'
    texto2 = '  NOME'

    if contador % 2 == 0:
        resultado = texto2 + str(contador)
        nome['text'] = texto2
        nome['bg'] = cor2
    
    else:
        resultado = texto1 + str(contador)
        nome['text'] = texto1
        nome['bg'] = cor3

    contador += 1

# label

nome = Label(janela, width=10, height=2, text='NOME', relief='groove', font='Arial 10', fg='black')
nome.grid(row=0, column=0, pady=8, padx=8)

# buttão

b_botao = Button(janela, width=10, text='Trocar', relief='groove', font='Arial 10', command=execultar)
b_botao.grid(row=0, column=1, padx=10) 



janela.mainloop()