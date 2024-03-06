from tkinter.ttk import *
from tkinter import *

# Configurando janela

janela = Tk()
janela.title("Combox")
janela.geometry("300x250")

#nome


label_nome = Label(janela, width=15, height=2, text="Faça sua escolha", font=("Arial 10"), anchor="w")
label_nome.grid(row=0, column=0, padx=5, sticky=NSEW)


# Criando combobox

combo = Combobox(janela)


# função do combobox

def obter():
    rsultado = combo.get()
    print(rsultado)
    print(f'Seja bem vindo {rsultado}')


# defenindo valores para combobox
combo['values'] = ('lucas', 'leticia', 'maicon', 'rafaela')

combo.grid(row=1, column=0, padx=5, sticky=NSEW)
combo.current(0)

#botão 

botao = Button(janela, width=10, height=1, text='ver resposta', relief='raised' , bg='white', command=obter)
botao.grid(row=2, column=0, padx=5, pady=20)



janela.mainloop()

