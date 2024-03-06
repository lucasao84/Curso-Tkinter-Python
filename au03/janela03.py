from tkinter import *

# cores 

cor1 = '#2E503C'     #Verde
cor2 = '#FFFFFF'     #Branco
cor3 = '#4D14B8'     #rocho
cor4 = '#B9DE3F'     #amarelo


# janela
janela = Tk()
janela.title('palce, pack, grid')
janela.geometry('400x500')
janela.config(bg=cor1)




# label

# exemplo.place(x = 10, y = 10)

# X move as laterais / horizontal
# Y move em baixo e em sima / vertical

# exemplo.pack(sIDE=RIGHT)

# side escolhe qual lado vai fica o label

# linha 1

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=0, column=0, padx=10, pady=10)

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=0, column=1, padx=10, pady=10)

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=0, column=2, padx=10, pady=10)

#llinha01.grid(row=1, column=inha 2

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=1, column=0,  padx=10, pady=10)

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=1, column=1, padx=10, pady=10)

linha01 = Label(janela, width=15, text='' , background=cor2)
linha01.grid(row=1, column=2, padx=10, pady=10)

#linha 3

linha01 = Label(janela, width=52, height=20, text='' , background=cor2)
linha01.place(x=10, y=90 )

janela.mainloop()




