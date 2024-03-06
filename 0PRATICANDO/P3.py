from tkinter import *


# Criando janela

janela = Tk()
janela.title('FORMULARIO')
janela.geometry('350x250')

# Criando Label e Entry





    



nome_label = Label(janela,text='Nome:' ,width=5, font='Arial 10', anchor='w')
nome_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

nome_entry = Entry(janela, width=20, font='Arial 10')
nome_entry.grid(row=0, column=1, sticky=NSEW ,padx=10, pady=10)

end_res = Label(janela, width=40, height=8, text='', bg='black', fg='#DEDAD7')
end_res.place(x=40, y=50, )


def obter():
    nome = nome_entry.get()

    end_res['text'] = nome 

botao = Button(janela, width=10, height=2, relief='groove', text='ENTER', command=obter)
botao.place(x=20, y=200)
janela.mainloop()

