import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt


load_dotenv()


# Cria uma nova conexão com o banco MySQL
def conectar():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        port=int(os.getenv('MYSQL_PORT'))
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
        return 'Livro já existente'

    cursor.execute(
        'INSERT INTO livros (nome, autor, disponivel) VALUES (%s, %s, %s)',
        (nome, autor, True)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    return 'Livro adicionado com sucesso'


# Busca informações de um livro específico
def buscar_livro(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
    'SELECT * FROM livros WHERE nome LIKE %s',
    (f'%{nome}%',)
    )
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

def registrar_emprestimo(cursor, id_livro, usuario):
    
    cursor.execute(
        '''
        INSERT INTO historico_emprestimos
        (id_livro, usuario)
        VALUES (%s, %s)
        ''',
        (id_livro, usuario)
    )
    

# Marca um livro como emprestado
def emprestar_livro(nome, usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT id_livro, disponivel FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    # Livro inexistente
    if resultado is None:
        cursor.close()
        conexao.close()
        return 'Livro inexistente'
    
    
    id_livro = resultado[0]
    disponivel = resultado[1]
    
    
    # Livro já emprestado
    if not disponivel:
        cursor.close()
        conexao.close()
        return 'Livro já emprestado'

    cursor.execute(
        'UPDATE livros SET disponivel = FALSE, usuario = %s WHERE id_livro = %s',
        (usuario, id_livro)
    )
    
    registrar_emprestimo(cursor, id_livro, usuario)
    
    conexao.commit()

    cursor.close()
    conexao.close()

    return 'Emprestado com sucesso'


# Marca um livro como disponível novamente
def devolver_livro(nome, usuario):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        'SELECT id_livro, disponivel, usuario FROM livros WHERE nome = %s',
        (nome,)
    )

    resultado = cursor.fetchone()

    # Livro inexistente
    if resultado is None:
        cursor.close()
        conexao.close()
        return 'Livro inexistente'
    
    id_livro = resultado[0]
    disponivel = resultado[1]
    dono_livro = resultado[2]
    
    # Livro já disponível
    if disponivel:
        cursor.close()
        conexao.close()
        return 'Livro já está disponível'

    if dono_livro != usuario:
        cursor.close()
        conexao.close()
        return 'Esse livro pertence a outro usuário'


    cursor.execute(
        'UPDATE livros SET disponivel = TRUE, usuario = NULL WHERE id_livro = %s',
        (id_livro,)
    )

    finalizar_emprestimo(cursor, id_livro)
    conexao.commit()

    cursor.close()
    conexao.close()

    return 'Livro devolvido com sucesso'

def finalizar_emprestimo(cursor, id_livro):

    cursor.execute(
        '''
        UPDATE historico_emprestimos
        SET data_devolucao = NOW()
        WHERE id_livro = %s
        AND data_devolucao IS NULL
        ''',
        (id_livro,)
    )
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

def listar_historico():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        '''
        SELECT
            livros.nome,
            historico_emprestimos.usuario,
            historico_emprestimos.data_emprestimo,
            historico_emprestimos.data_devolucao
            
        FROM historico_emprestimos
        
        INNER JOIN livros
        ON historico_emprestimos.id_livro = livros.id_livro
        '''
    )
    
    resultado = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return resultado
# Ver se é usuario ou adm
def buscar_tipo_usuario(usuario):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        'SELECT tipo FROM usuarios WHERE nome = %s',
        (usuario,)
    )

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    if resultado:
        return resultado[0].lower().strip()

    return None