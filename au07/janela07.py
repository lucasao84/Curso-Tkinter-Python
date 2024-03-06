from tkinter import * 

# Configurando Janela

janela = Tk()
janela.geometry('300x250')
janela.title("RadionButton")


# fFunçao do RadionButton

def obter():
    resultado = s1.get()

    print(resultado)

s1 = IntVar()
s2 = BooleanVar()
s3 = StringVar()

# RadionButton

radio1 = Radiobutton(janela, text='primeiro', value=1, command=obter , variable=s1)
radio1.grid(row=0, column=0, padx=10, pady=10)
                    
radio2 = Radiobutton(janela, text='segundo', value=2, command=obter, variable=s1)
radio2.grid(row=1, column=0, padx=10, pady=10)

radio3 = Radiobutton(janela, text='terceiro', value=3, command=obter, variable=s1)
radio3.grid(row=2, column=0, padx=10, pady=10)



janela.mainloop()