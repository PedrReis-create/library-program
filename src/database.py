import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pedro123',
    database = 'biblioteca',
    port = 3307
)
def cadastrar_usuarios(usuario, senha):
    cursor = conexao.cursor()
    
    # verifica se já existe
    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s',
        (usuario,)
    )
    resultado = cursor.fetchone()
    
    if resultado :
        return False
    
    # se chegou aqui, não existe, então cadastra
    cursor.execute(
        'INSERT into usuarios (nome, senha) VALUES (%s, %s)',
        (usuario, senha)
    )
    
    conexao.commit()
    
    return True

def verificar_usuario(usuario, senha):
    cursor  = conexao.cursor()
    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s AND senha = %s',
        (usuario, senha)
    )
    resultado = cursor.fetchone()
    
    return resultado is not None

def adicionar_livro(nome, autor):
    cursor = conexao.cursor()
    
    cursor.execute(
        'INSERT INTO livros (nome, autor, disponivel) VALUES(%s, %s, %s)',
        (nome, autor, True)
    )
    conexao.commit()

def buscar_livro(nome):
    cursor = conexao.cursor()
    
    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )
    resultado = cursor.fetchone()
    return resultado

