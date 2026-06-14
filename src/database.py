import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt


load_dotenv()


# Cria uma nova conexão com o banco MySQL
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('MYSQL_PASSWORD'),
        database='biblioteca',
        port=3307
    )


# Cadastra um novo usuário com senha criptografada
def cadastrar_usuarios(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    # Verifica se o usuário já existe
    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s',
        (usuario,)
    )

    resultado = cursor.fetchone()

    if resultado:
        cursor.close()
        conexao.close()
        return False

    # Cria hash seguro da senha antes de salvar
    senha_hash = bcrypt.hashpw(
        senha.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    cursor.execute(
        'INSERT INTO usuarios (nome, senha) VALUES (%s, %s)',
        (usuario, senha_hash)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return True


# Verifica login comparando a senha com o hash salvo
def verificar_usuario(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT senha FROM usuarios WHERE nome = %s',
        (usuario,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado is None:
        return False

    senha_hash = resultado[0]

    if isinstance(senha_hash, str):
        senha_hash = senha_hash.encode('utf-8')

    return bcrypt.checkpw(
        senha.encode('utf-8'),
        senha_hash
    )


# Adiciona um novo livro no banco
def adicionar_livro(nome, autor):
    conexao = conectar()
    cursor = conexao.cursor()

    # Impede cadastro duplicado
    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    if resultado:
        cursor.close()
        conexao.close()
        return False

    cursor.execute(
        'INSERT INTO livros (nome, autor, disponivel) VALUES (%s, %s, %s)',
        (nome, autor, True)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return True


# Busca informações de um livro específico
def buscar_livro(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado


# Marca um livro como emprestado
def emprestar_livro(nome, usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT disponivel FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    # Livro inexistente
    if resultado is None:
        cursor.close()
        conexao.close()
        return False

    # Livro já emprestado
    if resultado[0] is False:
        cursor.close()
        conexao.close()
        return False

    cursor.execute(
        'UPDATE livros SET disponivel = FALSE, usuario = %s WHERE nome = %s',
        (usuario, nome)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return True


# Marca um livro como disponível novamente
def devolver_livro(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT disponivel FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    # Livro inexistente
    if resultado is None:
        cursor.close()
        conexao.close()
        return False

    # Livro já disponível
    if resultado[0] is True:
        cursor.close()
        conexao.close()
        return False

    cursor.execute(
        'UPDATE livros SET disponivel = TRUE, usuario = NULL WHERE nome = %s',
        (nome,)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return True


# Retorna todos os livros cadastrados
def listar_livro():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT * FROM livros'
    )

    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado