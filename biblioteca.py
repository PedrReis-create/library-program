# biblioteca.py

livros = [
    {
        'nome': 'Harry Potter',
        'disponivel': True,
        'usuario': None
    },
    {
        'nome': '1984',
        'disponivel': True,
        'usuario': None
    }
]


def emprestar_livro(nome_livro, usuario):
    if not usuario:
                return 'Digite seu nome primeiro'
                return
    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():
            
            if livro['disponivel']:

                livro['disponivel'] = False
                livro['usuario'] = usuario

                return'Livro emprestado com sucesso!'
                return
            else:
                return 'Livro já emprestado'
                return

    return 'Livro não encontrado!'


def devolver_livro(nome_livro):

    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            if not livro['disponivel']:

                livro['disponivel'] = True
                livro['usuario'] = None

                return 'Livro devolvido!'
                return

            else:
                return'Esse livro já está disponível.'

    return'Livro não encontrado!'


def adicionar_livro(nome_livro):
    if not nome_livro:
        return 'Adicione um livro válido'
        return
    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            return'Livro já existe!'
            return

    livros.append({
        'nome': nome_livro,
        'disponivel': True,
        'usuario': None
    })

    return 'Livro adicionado com sucesso!'

def listar_livros():

    lista_dos_livros = ''
    
    for livro in livros:
        status = 'Disponível' if livro['disponivel'] else 'Emprestado'
        lista_dos_livros += f"Livro: {livro['nome'] }\n Status: {status}\n Usuário: {livro['usuario']}\n\n "


    return lista_dos_livros