from tkinter import *
from tkinter import ttk
from biblioteca import *

# Inicializar
myApp = Tk()

# Título
myApp.title("Biblioteca")

# Ícone
myApp.iconbitmap("book.ico")

# Dimensões
myApp.geometry("300x300")
myApp.resizable(False, False)

# Cor
myApp.configure(background='white')


# Funções
def procurar_livro():
    nome = entrada_livro.get().strip()

    resultado = buscar_livro(nome)

    resultado_label.config(text=resultado)


# Texto
showinfo = ttk.Label(
    myApp,
    text='Nome do livro:',
    background='white'
)
showinfo.place(x=100, y=40)

# Entrada
entrada_livro = ttk.Entry(myApp)
entrada_livro.place(x=70, y=70, width=160, height=25)

# Botão
botao1 = ttk.Button(
    myApp,
    text='Procurar',
    command=procurar_livro
)
botao1.place(x=110, y=120, width=80)

# Resultado
resultado_label = Label(
    myApp,
    text='',
    bg='white',
    justify='center',
    font=('Arial', 10)
)

resultado_label.place(x=50, y=180, width=200)

# Loop
myApp.mainloop()
