from tkinter import *

# cores 

cor1 = '#2E503C'     #Verde
cor2 = '#FFFFFF'     #Branco
cor3 = '#4D14B8'     #rocho
cor4 = '#B9DE3F'     #amarelo

# criando janelas

janela = Tk()
janela.title('TABELA')
janela.geometry('300x300')


# criando label

label_nome = Label(janela, width=10, text='NOME : ', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=0, column=0, pady=2, padx=2)
label_nome = Label(janela, width=10, text='LUCAS', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=0, column=1, pady=0 , padx=0)

label_nome = Label(janela, width=10, text='IDADE : ', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=1, column=0, pady=2 , padx=2)
label_nome = Label(janela, width=10, text='25', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=1, column=1, pady=0 , padx=0)

label_nome = Label(janela, width=10, text='PAIS : ', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=2, column=0, pady=2 , padx=2)
label_nome = Label(janela, width=10, text='BRASIL', background='black', fg=cor2, font='Arial 10')
label_nome.grid(row=2, column=1, pady=0 , padx=0)


janela.mainloop()