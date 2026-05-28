#aqui é a interface com tkinter
import tkinter as tk
from biblioteca import emprestar_livro

def iniciar_interface():
    janela = tk.Tk()

    janela.title('Sistema de biblioteca')
    
    botao_emprestar = tk.Button(
        janela,
        text='Pegar livro emprestado',
        command=emprestar_livro
    )
    botao_emprestar.pack()
    janela.mainloop()