from tkinter import *
from tkinter import ttk
from biblioteca import *

usuario_atual = None
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
    nomebook = entrada_livro.get().strip()

    resultado = buscar_livro(nomebook)

    resultado_label.config(text=resultado)

def emprestar():
    nome = entrada_livro.get().strip()

    resultado = emprestar_livro(
        nome,
        usuario_atual
    )

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

# Botão 1
botao1 = ttk.Button(
    myApp,
    text='Procurar',
    command=procurar_livro
)
botao1.place(x=110, y=120, width=80)

# Botão 2
botao2 = ttk.Button(
    myApp,
    text ='Emprestar',
    command=emprestar
)
botao2.place(x=100, y=210, width=80)
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
