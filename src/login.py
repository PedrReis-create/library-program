import tkinter as tk
from tkinter import ttk
from database import (
    cadastrar_usuarios,
    verificar_usuario,
    buscar_tipo_usuario
)

# Inicializar
janela = tk.Tk()

# Título
janela.title("Biblioteca")

# Ícone
try:
    janela.iconbitmap("book.ico")
except:
    pass

# Dimensões
width = 300
height = 300

width_tela = janela.winfo_screenwidth()
height_tela = janela.winfo_screenheight()

pos_x = (width_tela // 2) - (width // 2)
pos_y = (height_tela // 2) - (height // 2)

janela.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
janela.resizable(False, False)


def abrir_biblioteca(usuario, tipo):
    janela.destroy()

    import interface
    interface.usuario_atual = usuario
    interface.abrir(usuario, tipo)


# Função de cadastro
def cadastrar():
    nome = entrada_nome.get().strip().capitalize()
    senha = entrada_senha.get().strip()
    
    if not nome or not senha :
        resultado.config(text='Preencha todos os campos! ')
        return
    if len(senha) < 8 :
        resultado.config(text='Crie uma senha com mais de 4 dígitos! ')
        return
    elif len(senha) > 20 :
        resultado.config(text='Crie uma senha com menos de 20 dígitos! ')
        return

    if cadastrar_usuarios(nome, senha):
        resultado.config(text='Cadastro realizado com sucesso! ')
        abrir_biblioteca(nome, "usuario")
    else:
        resultado.config(text='Usuário já existe! ')

# Função para entrar ao inves de fazer o login
def entrar():
    
    nome = entrada_nome.get().strip().capitalize()
    senha = entrada_senha.get().strip()

    if not nome or not senha:
        resultado.config(text="Preencha todos os campos!")
        return

    if verificar_usuario(nome, senha):

        tipo = buscar_tipo_usuario(nome)

        resultado.config(
            text=f"Bem-vindo, {nome}!"
        )

        abrir_biblioteca(nome, tipo)
    else:
        resultado.config(text="Nome ou senha incorretos!")


# Nome
ttk.Label(janela, text="Nome").pack(pady=5)
entrada_nome = ttk.Entry(janela)
entrada_nome.pack()

# Senha
ttk.Label(janela, text="Senha").pack(pady=5)
entrada_senha = ttk.Entry(janela, show="*")
entrada_senha.pack()

# Botões
ttk.Button(janela, text="Entrar", command=entrar).pack(pady=5)
ttk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)

# Mensagem
resultado = ttk.Label(janela, text="")
resultado.pack(pady=10)

janela.mainloop()
