import tkinter as tk
from tkinter import ttk

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


def abrir_biblioteca(usuario):
    janela.destroy()

    import interface
    interface.usuario_atual = usuario
    interface.abrir(usuario)


# Função de cadastro
def cadastrar():
    nome = entrada_nome.get().capitalize()
    senha = entrada_senha.get()

    if nome == "" or senha == "":
        resultado.config(text="Preencha todos os campos!")
        return

    if len(senha) < 4:
        resultado.config(text="Crie um senha com mais de 4 digitos!")
        return

    elif len(senha) > 20:
        resultado.config(text="Crie um senha com menos de 20 digitos!")
        return

    # Verifica se o usuário já existe
    try:
        with open("login_da_biblioteca.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                usuario, _ = linha.strip().split(";")

                if usuario == nome:
                    resultado.config(text="Usuário já cadastrado!")
                    return

    except FileNotFoundError:
        pass

    # Salva o novo usuário
    with open("login_da_biblioteca.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{senha}\n")

    resultado.config(text="Cadastro realizado!")
    abrir_biblioteca(nome)


# Função para entrar ao inves de fazer o login
def entrar():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if nome == "" or senha == "":
        resultado.config(text="Preencha todos os campos!")
        return

    try:
        with open("login_da_biblioteca.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                usuario, senha_salva = linha.strip().split(";")

                if usuario == nome and senha_salva == senha:
                    resultado.config(text=f"Bem-vindo, {nome}!")
                    abrir_biblioteca(nome)
                    return

        resultado.config(text="Nome ou senha incorretos!")

    except FileNotFoundError:
        resultado.config(text="Nenhum usuário cadastrado!")


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
