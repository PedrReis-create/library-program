# biblioteca.py

livros = [
    {
        'nome': 'Harry potter',
        'disponivel': True,
        'usuario': None
    },
]

def buscar_livro(nome_livro):
    if not nome_livro : return'Digite um nome válido'
    if len(livros) == 0:
        return 'Nenhum livro encontrado.'

    for k, livro in enumerate(livros):
        if livro['nome'].lower() == nome_livro.lower():
            return (
                f"ID: {k}\n"
                f"Nome: {livro['nome']}\n"
                f"Disponível: {'Sim' if livro['disponivel'] else 'Não'}"
            )

    return 'Nenhum livro encontrado.'

def emprestar_livro(nome_livro, usuario):
    if not nome_livro : return'Digite um nome válido'
    
    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            if livro['disponivel']:

                livro['disponivel'] = False
                livro['usuario'] = usuario

                return'Livro emprestado com sucesso!'
                

            else:
                return'Livro já emprestado!'
                

    return'Livro não encontrado!'


def devolver_livro(nome_livro):
    if not nome_livro : return('Digite um nome válido')
    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            if not livro['disponivel']:

                livro['disponivel'] = True
                livro['usuario'] = None

                return 'Livro devolvido!'
                

            else:
                return'Esse livro já está disponível.'
                

    return'Livro não encontrado!'


def adicionar_livro(nome_livro):
    if not nome_livro : return'Digite um nome válido'
    for livro in livros:

        if livro['nome'].lower() == nome_livro.lower():

            return'Livro já existe!'
            

    livros.append({
        'nome': nome_livro,
        'disponivel': True,
        'usuario': None
    })

    return'Livro adicionado com sucesso!'


def listar_livros():

    for livro in livros:

        status = 'Disponível' if livro['disponivel'] else 'Emprestado'

        return(f'''
Nome: {livro['nome']}
Status: {status}
Usuário: {livro['usuario']}
''')