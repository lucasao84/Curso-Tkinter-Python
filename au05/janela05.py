from tkinter import *

# Criando janela

janela = Tk()
janela.title('AULA05')
janela.geometry('400x250')

# CRIANDO LABEL, ENTRY

# NOME
nome = Label(janela , width=8, text='NOME : ' , anchor='w')
nome.grid(row=0, column=0, padx=4, pady=4, sticky=NSEW)
entry_nome = Entry(janela, width=15, font=('Arial 10'), state='disabled')
entry_nome.grid(row=0, column=1,pady=4)

# IDADE
nome = Label(janela , width=8, text='IDADE : ', anchor='w')
nome.grid(row=1, column=0, padx=4, pady=4, sticky=NSEW)
entry_idade = Entry(janela, width=15, font=('Arial 10'))
entry_idade.grid(row=1, column=1,pady=4)

# PAIS
nome = Label(janela , width=8, text='PAIS : ', anchor='w')
nome.grid(row=2, column=0, padx=4, pady=4, sticky=NSEW)
entry_pais = Entry(janela, width=15, font=('Arial 10'))
entry_pais.grid(row=2, column=1,pady=4)

# Respostas

res_nome = Label(janela , width=20, text='' , font='Arial 8', anchor='w')
res_nome.grid(row=0, column=3, padx=4, pady=4, sticky=NSEW)

res_idade = Label(janela , width=15, text='', font='Arial 8', anchor='w')
res_idade.grid(row=1, column=3, padx=4, pady=4, sticky=NSEW)

res_pais = Label(janela , width=15, text='', font='Arial 8', anchor='w')
res_pais.grid(row=2, column=3, padx=4, pady=4, sticky=NSEW)

#funçao obter dados

def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    res_nome['text'] = nome
    res_idade['text'] = idade
    res_pais['text'] = pais

# Para limpa os dados dentro da entry
    entry_nome.delete(0,END)
    entry_idade.delete(0,END)
    entry_pais.delete(0, END)
    


# Botao

botao = Button(janela, width=10, text='Ver dados', height=2, relief='groove', command=obter)
botao.grid(row=3, column=0, padx=10, pady=10)

janela.mainloop()

