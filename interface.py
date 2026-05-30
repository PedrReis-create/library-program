#interface
import tkinter as tk
from biblioteca import emprestar_livro
from biblioteca import devolver_livro
from biblioteca import adicionar_livro
from biblioteca import listar_livros

def criar_interface(janela):
    app_sistema = tk.Frame(janela)

    tk.Label(app_sistema, text='Sistema biblioteca').pack()

    tk.Label(app_sistema, text='Digite seu nome: ').pack()
    usuario_name = tk.Entry(app_sistema)
    usuario_name.pack()

    tk.Label(app_sistema, text='Nome do livro: ').pack() #onde mostra todos os resultados
    livro_get = tk.Entry(app_sistema)
    livro_get.pack()


    #function emprestar livro
    def emprestar_livro_interface():
        book= livro_get.get()
        usuario= usuario_name.get()
        mensagem= emprestar_livro(book, usuario)
        mensagem_label['text'] = mensagem
        livro_get.delete(0, tk.END)
    btnE = tk.Button(app_sistema,
        text='Emprestar', 
        command=emprestar_livro_interface
    )
    btnE.pack()

    #function devolver livro
    def devolver_livro_interface():
        book = livro_get.get()
        mensagem = devolver_livro(book)
        mensagem_label['text'] = mensagem
        livro_get.delete(0, tk.END)
    btnD = tk.Button(app_sistema,
        text='Devolver',
        command=devolver_livro_interface
    )
    btnD.pack()

    #function adicionar livro
    def adicionar_livro_interface():
        book = livro_get.get()
        mensagem = adicionar_livro(book)
        mensagem_label['text'] = mensagem
        livro_get.delete(0, tk.END)
    btnA = tk.Button(app_sistema,
        text='Adicionar',
        command=adicionar_livro_interface
    )
    btnA.pack()

    #function listar livros
    def listar_livros_interface():
        mensagem = listar_livros()
        mensagem_label['text'] = mensagem
    btnL = tk.Button(app_sistema,
        text='Listar',
        command=listar_livros_interface
    )
    btnL.pack()

    mensagem_label = tk.Label(app_sistema)
    mensagem = ''
    mensagem_label['text'] = mensagem
    mensagem_label.pack()
    return app_sistema



