from tkinter import * 

# Cores 

cor1 = '#2E503C'     #Verde
cor2 = '#FFFFFF'     #Branco
cor3 = '#4D14B8'     #rocho
cor4 = '#B9DE3F'     #amarelo

# Config padrao do tkinter

janela =Tk()
janela.title('Label')
janela.geometry('400x500')
janela.config(bg=cor1)

# Label

#pady / atributo para dar espaçamento
#grid / atributo para posionar o label em linha e coluna


#nome

label_nome = Label(janela, width=10, text='NOME : ', bg=cor1, fg=cor2, font='Arial 15', background='black')
label_nome.grid(row=0, column=0, padx=10, pady=10)

#idade

label_idade = Label(janela, width=10, text='IDADE : ', bg=cor1, fg=cor3, font='Arial 15', background='black' )
label_idade.grid(row=1, column=0, padx=10, pady=10)

#pais

label_pais = Label(janela, width=10, text='PAIS : ', bg=cor1, fg=cor4, font='Arial 15', background='black' )
label_pais.grid(row=2, column=0, padx=10, pady=10)

janela.mainloop()