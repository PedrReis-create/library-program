import tkinter as tk
from biblioteca import emprestar_livro

janela = tk.Tk()
janela.title('Sistema de biblioteca')

showinfo = tk.Label(janela, text='Nome do livro:')
showinfo.pack()

entrada_livro = tk.Entry(janela)

entrada_usuario = tk.Entry(janela)

entrada_livro.pack()
entrada_usuario.pack()

def emprestar_livro_interface():
    nome_livro = entrada_livro.get()
    usuario = entrada_usuario.get()
    emprestar_livro(nome_livro, usuario)
    
botao1 = tk.Button(
    janela,
    text='Emprestar',
    command=emprestar_livro_interface
)

botao1.pack()

janela.mainloop()