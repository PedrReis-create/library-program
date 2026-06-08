from tkinter import *
from tkinter import ttk
from database import (
    adicionar_livro,
    buscar_livro,
    emprestar_livro,
    devolver_livro,
    listar_livro
)  # COMEÇANDO A CONECTAR FUNCOES AO DATABASE


# Inicializar
def abrir(usuario):
    myApp = Tk()
    # Título
    myApp.title("Biblioteca")

    # Ícone
    myApp.iconbitmap("book.ico")

    # Dimensões
    largura = 300
    altura = 300

    largura_tela = myApp.winfo_screenwidth()
    altura_tela = myApp.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    myApp.geometry(f"{largura}x{altura}+{x}+{y}")

    # Cor
    myApp.configure(background='white')


    # Funções

    def mostrar_resultado(texto):
        resultado_label.config(text=texto)

    def procurar_livro():
        nome = entrada_livro.get().strip()

        resultado = buscar_livro(
            nome
        )

        mostrar_resultado(resultado)

    def emprestar():
        nome = entrada_livro.get().strip()
        if usuario is None:
            mostrar_resultado('Faça login primeiro')
            return
        resultado = emprestar_livro(nome)

        mostrar_resultado(resultado)

    def devolver():
        nome = entrada_livro.get().strip()
        resultado = devolver_livro(
            nome
        )

        mostrar_resultado(resultado)

    def adicionar():
        nome = entrada_livro.get().strip()
        autor = entrada_livro.get().strip()
        resultado = adicionar_livro(
            nome,
            autor
        )
        
        mostrar_resultado(resultado)

    def listar():
        resultado = listar_livro()
        mostrar_resultado(resultado)
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
    
    # Para a função adicionar livro
    entrada_autor = ttk.Entry(myApp)
    entrada_livro.place()

    # Botão 1 Procurar Livro
    botao1 = ttk.Button(
        myApp,
        text='Procurar',
        command=procurar_livro
    )
    botao1.place(x=45, y=120, width=70)

    # Botão 2 Emprestar Livro
    botao2 = ttk.Button(
        myApp,
        text ='Emprestar',
        command=emprestar
    )
    botao2.place(x=115, y=120, width=70,)

    # Botão 3 Devolver Livro
    botao3 = ttk.Button(
        myApp,
        text='Devolver',
        command=devolver  
    )
    botao3.place(x=185, y=120, width=70)

    # Botão 4 Adicionar Livro
    botao4 = ttk.Button(
        myApp,
        text='Adicionar',
        command=adicionar
    )
    botao4.place(x=80, y=145, width=70)

    # Botão 5 Listar Livros
    botao5 = ttk.Button(
        myApp,
        text='Listar',
        command=listar   
    )
    botao5.place(x=150, y=145, width=70)

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
