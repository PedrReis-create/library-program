import tkinter as tk
from biblioteca import emprestar_livro
from biblioteca import devolver_livro
from biblioteca import adicionar_livro
from biblioteca import listar_livros


janela = tk.Tk()
janela.title('Sistema de biblioteca')
janela.geometry('400x300')

app_sistema = tk.Frame(janela)
app_sistema.pack()

tk.Label(app_sistema, text='Sistema biblioteca').pack()

tk.Label(app_sistema, text='Digite seu nome: ').pack()
usuario_name = tk.Entry(app_sistema)
usuario_name.pack()

tk.Label(app_sistema, text='Nome do livro: ').pack() #onde mostra todos os resultados
livro_get = tk.Entry(app_sistema)
livro_get.pack()

def emprestar_livro_interface():
    book= livro_get.get()
    usuario= usuario_name.get()
    emprestar_livro(book, usuario)
btnE = tk.Button(app_sistema,
    text='Emprestar', 
    command=emprestar_livro_interface
)
btnE.pack()

janela.mainloop()

