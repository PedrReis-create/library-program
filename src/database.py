import mysql.connector

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'pedro123',
    database = 'biblioteca',
    port = 3307
)


# Cadastra novos usuários no banco
def cadastrar_usuarios(usuario, senha):
    cursor = conexao.cursor()
    
    # Verifica se o usuário já existe
    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s',
        (usuario,)
    )

    resultado = cursor.fetchone()
    
    # Se encontrou algum usuário, cancela o cadastro
    if resultado :
        return False
    
    # Insere o novo usuário
    cursor.execute(
        'INSERT into usuarios (nome, senha) VALUES (%s, %s)',
        (usuario, senha)
    )
    
    # Salva a alteração no banco
    conexao.commit()
    
    return True


# Confere se o nome e senha existem para fazer login
def verificar_usuario(usuario, senha):
    cursor  = conexao.cursor()

    cursor.execute(
        'SELECT * FROM usuarios WHERE nome = %s AND senha = %s',
        (usuario, senha)
    )

    resultado = cursor.fetchone()
    
    # Retorna True se encontrou o usuário
    return resultado is not None


# Adiciona um livro novo no banco
def adicionar_livro(nome, autor):
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
    cursor = conexao.cursor()
    
    cursor.execute(
        'SELECT * FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    return resultado


# Marca um livro como emprestado
def emprestar_livro(nome):
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
        'UPDATE livros SET disponivel = FALSE WHERE nome = %s',
        (nome,)
    )
    
    conexao.commit()
    
    return True
    

# Marca um livro como disponível novamente
def devolver_livro(nome):
    cursor = conexao.cursor()
    
    cursor.execute(
        'UPDATE livros SET disponivel = TRUE WHERE nome = %s',
        (nome,)
    )
    
    conexao.commit()