import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()

# Conexão com o banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password=os.getenv('MYSQL_PASSWORD'),
        database='biblioteca',
        port=3307
    )


# Cadastra novos usuários no banco
def cadastrar_usuarios(usuario, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Verifica se o usuário já existe
    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s',
        (usuario,)
    )

    resultado = cursor.fetchone()
    
    # Se encontrou algum usuário, cancela o cadastro
    if resultado:
        cursor.close()
        conexao.close()
        return False
    
    # Insere o novo usuário
    senha_hash = bcrypt.hashpw(
        senha.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')
    
    cursor.execute(
        'INSERT into usuarios (nome, senha) VALUES (%s, %s)',
        (usuario, senha_hash)
    )
    
    # Salva a alteração no banco
    conexao.commit()

    cursor.close()
    conexao.close()

    return True


# Confere se o nome e senha existem para fazer login
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
    


# Adiciona um livro novo no banco
def adicionar_livro(nome, autor):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Verifica se o livro já existe
    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()
    
    # Impede livros repetidos
    if resultado :
        return False
    
    # Cadastra o livro como disponível
    cursor.execute(
        'INSERT INTO livros (nome, autor, disponivel) VALUES(%s, %s, %s)',
        (nome, autor, True)
    )

    conexao.commit()

    return True


# Busca um livro pelo nome
def buscar_livro(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    return resultado


# Marca um livro como emprestado
def emprestar_livro(nome, usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    # Consulta se o livro existe e se está disponível
    cursor.execute(
        'SELECT disponivel FROM livros WHERE nome = %s',
        (nome,)
    )
    
    resultado = cursor.fetchone()

    # Livro não encontrado
    if resultado is None:
        return False
    
    # Livro já está emprestado
    elif resultado[0] == False:
        return False
    
    # Atualiza disponibilidade para emprestado
    cursor.execute(
        'UPDATE livros SET disponivel = FALSE, usuario = %s WHERE nome = %s',
        (usuario, nome)
    )
    
    conexao.commit()
    
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

    # Livro não existe
    if resultado is None:
        return False

    # Livro já está disponível
    elif resultado[0] == True:
        return False

    cursor.execute(
        'UPDATE livros SET disponivel = TRUE, usuario = NULL WHERE nome = %s',
        (nome,)
    )

    conexao.commit()

    return True

#Lista os livros existentes
def listar_livro():
    conexao = conectar()
    cursor = conexao.cursor()
    
    #Selectiona tudo da coluna livros
    cursor.execute(
        'SELECT * FROM livros'
    )

    resultado = cursor.fetchall()

    return resultado