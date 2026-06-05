# biblioteca.py

livros = [
    {
        'nome': 'Harry potter',
        'disponivel': True,
        'usuario': None
    },
    {
        'nome': '1984',
        'disponivel': True,
        'usuario': None
    }
]

def buscar_livro(nome):
    if len(livros) == 0:
        return 'Nenhum livro encontrado.'

    for k, livro in enumerate(livros):
        if livro['nome'].lower() == nome.lower():
            return (
                f"ID: {k}\n"
                f"Nome: {livro['nome']}\n"
                f"Disponível: {'Sim' if livro['disponivel'] else 'Não'}"
            )

    return ('Nenhum livro encontrado.')

def emprestar_livro(nome_livro, usuario):

    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            if livro['disponivel']:

                livro['disponivel'] = False
                livro['usuario'] = usuario

                print('Livro emprestado com sucesso!')
                return

            else:
                print('Livro já emprestado!')
                return

    print('Livro não encontrado!')


def devolver_livro(nome_livro):

    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            if not livro['disponivel']:

                livro['disponivel'] = True
                livro['usuario'] = None

                print('Livro devolvido!')
                return

            else:
                print('Esse livro já está disponível.')
                return

    print('Livro não encontrado!')


def adicionar_livro(nome_livro):

    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            print('Livro já existe!')
            return

    livros.append({
        'nome': nome_livro,
        'disponivel': True,
        'usuario': None
    })

    print('Livro adicionado com sucesso!')


def listar_livros():

    for livro in livros:

        status = 'Disponível' if livro['disponivel'] else 'Emprestado'

        print(f'''
Nome: {livro['nome']}
Status: {status}
Usuário: {livro['usuario']}
''')