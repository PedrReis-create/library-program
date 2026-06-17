from tkinter import *
from tkinter import ttk
from database import (
    adicionar_livro,
    buscar_livro,
    emprestar_livro,
    devolver_livro,
    listar_livro
)


def abrir(usuario, tipo):

    myApp = Tk()

    myApp.title("Biblioteca")
    myApp.iconbitmap("book.ico")

    largura = 900
    altura = 500

    largura_tela = myApp.winfo_screenwidth()
    altura_tela = myApp.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    myApp.geometry(f"{largura}x{altura}+{x}+{y}")
    myApp.configure(background='white')

    usuario_label = Label(
        myApp,
        text=f'Logado: {usuario} ({tipo})',
        bg='white',
        font=('Arial', 10, 'bold')
    )

    usuario_label.place(
        x=650,
        y=20
    )
    # =================
    # Funções
    # =================
    
    def sair():

        myApp.destroy()

        print('Obrigado por usar nosso sistema')

    
    def mostrar_resultado(texto):
        resultado_label.config(text=texto)
    def limpar_campos():

        entrada_livro.delete(0, END)
        entrada_autor.delete(0, END)


    def procurar_livro():

        nome = entrada_livro.get().strip()

        livro = buscar_livro(nome)

        for item in tabela.get_children():
            tabela.delete(item)

        if livro:

            tabela.insert(
                '',
                END,
                values=(
                    livro[1],
                    livro[2],
                    'Disponível' if livro[3] else 'Emprestado',
                    livro[4]
                )
            )

        else:
            mostrar_resultado('Livro não encontrado!')


    def emprestar():
        
        nome = entrada_livro.get().strip()
        if not nome:
            mostrar_resultado('Digite um livro!')
            return
        if usuario is None:
            mostrar_resultado('Faça login primeiro!')
            return

        elif emprestar_livro(nome, usuario):
            mostrar_resultado('Livro emprestado!')
            limpar_campos()
            listar()

        else:
            mostrar_resultado('Não foi possível emprestar!')


    def devolver():

        nome = entrada_livro.get().strip()

        if devolver_livro(nome):
            mostrar_resultado('Livro devolvido!')
            limpar_campos()
            listar()

        else:
            mostrar_resultado('Não foi possível devolver!')


    def adicionar():
        if tipo != "admin":
            mostrar_resultado(
                "Apenas administradores podem adicionar livros!"
            )
            return
        
        nome = entrada_livro.get().strip()
        autor = entrada_autor.get().strip()

        if not nome or not autor :
            mostrar_resultado('Coloque um nome válido')
            return
        elif adicionar_livro(nome, autor):
            mostrar_resultado('Livro adicionado!')
            limpar_campos()
            listar()
        else:
            mostrar_resultado('Livro já existente')


    def listar():

        for item in tabela.get_children():
            tabela.delete(item)

        livros = listar_livro()

        for livro in livros:

            tabela.insert(
                '',
                END,
                values=(
                    livro[1],
                    livro[2],
                    'Disponível' if livro[3] else 'Emprestado',
                    livro[4]
                )
            )


    # =================
    # Interface
    # =================


    showinfo = ttk.Label(
        myApp,
        text='Nome do livro:',
        background='white'
    )

    showinfo.place(
        x=80,
        y=30
    )


    entrada_livro = ttk.Entry(myApp)

    entrada_livro.place(
        x=180,
        y=28,
        width=250,
        height=25
    )


    showauthor = ttk.Label(
        myApp,
        text='Nome do autor:',
        background='white'
    )

    showauthor.place(
        x=80,
        y=70
    )


    entrada_autor = ttk.Entry(myApp)

    entrada_autor.place(
        x=180,
        y=68,
        width=250,
        height=25
    )

    botao_sair = ttk.Button(
    myApp,
    text='Sair',
    command=sair
    )

    botao_sair.place(
        x=760,
        y=60,
        width=90
    )

    botao1 = ttk.Button(
        myApp,
        text='Procurar',
        command=procurar_livro
    )

    botao1.place(
        x=60,
        y=120,
        width=90
    )


    botao2 = ttk.Button(
        myApp,
        text='Emprestar',
        command=emprestar
    )

    botao2.place(
        x=160,
        y=120,
        width=90
    )


    botao3 = ttk.Button(
        myApp,
        text='Devolver',
        command=devolver
    )

    botao3.place(
        x=260,
        y=120,
        width=90
    )


    botao4 = ttk.Button(
        myApp,
        text='Adicionar',
        command=adicionar
    )

    botao4.place(
        x=360,
        y=120,
        width=90
    )
    
    if tipo != "admin":

        botao4.config(
            state="disabled"
        )
        
    resultado_label = Label(
        myApp,
        text='',
        bg='white',
        font=('Arial', 10)
    )

    resultado_label.place(
    x=330,
    y=180,
    width=250,
    height=30
    )


    tabela = ttk.Treeview(
        myApp,
        columns=('Nome', 'Autor', 'Status', 'Usuario'),
        show='headings'
    )


    tabela.heading(
        'Nome',
        text='Nome'
    )

    tabela.heading(
        'Autor',
        text='Autor'
    )

    tabela.heading(
        'Status',
        text='Status'
    )

    tabela.heading(
        'Usuario',
        text='Usuário'
    )


    tabela.column(
        'Nome',
        width=170
    )

    tabela.column(
        'Autor',
        width=170
    )

    tabela.column(
        'Status',
        width=100
    )

    tabela.column(
        'Usuario',
        width=100
    )


    tabela.place(
    x=40,
    y=230,
    width=820,
    height=200
    )

    listar()

    myApp.mainloop()
