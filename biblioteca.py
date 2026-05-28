#fica o code
import sys
livros = [
        {
            'nome': 'Harry Potter',
            'disponivel': True,
            'usuario': None
        },
        {   'nome': '1984',
            'disponivel': True,
            'usuario': None
        }
]
  
def emprestar_livro(): #1
    print('Bem vindo a sessão Emprestar livros!(Você vai devolver, né?)')
    nome = input('Digite o nome do livro: ')
    
    for livro in livros :
        if livro['nome'].lower() == nome.lower() and livro['disponivel']:
            livro['disponivel'] = False
            livro['usuario'] = usuario
            print('Livro emprestado com sucesso')
            return
    
    print('Livro não disponível')

def listar_livros(): #2
    print('Bem vindo a sessão Listar livros!(Vai me fazer listar todos? Tenha dó)')
    for livro in livros: 
        if livro['disponivel']:
            print(livro['nome'])

def adicionar_livro(): #3
    print('Bem vindo a sessão Adicionar livros!(Virou bibliotecária foi?)')
    nome = input('Ms.Bibliotecária Pythonica, digite o nome do livro que gostaria de adicionar: ')
    
    for livro in livros :
        if livro['nome'].lower() == nome.lower():
            print('Livro já existente!')
            return
    
    livros.append({
        'nome' : nome,
        'disponivel' : True
    })
    print('Livro adicionado!')

def devolver_livro(): #4
    print('Bem vindo a sessão Devolver livro!(Você veio devolver mesmo! Uhulll)')
    devolver = input('Qual livro gostaria de devolver: ')
    
    for livro in livros :
        if livro['nome'] == devolver and not livro['disponivel']:
            livro['disponivel'] = True
            livro['usuario'] = None
            print('Livro Devolvido com sucesso')
            return

def sair(): #5
    print('Quer ir embora? Mas já?')
    print('Bom, foi bom enquanto durou...')
    print('<Saindo>')
    sys.exit()

def mainMenu():
    while True :
        acao = int(input(f'''\n O que deseja fazer, {usuario}?
        [1] Emprestar livro
        [2] Listar livros
        [3] Adicionar livros
        [4] Devolver livro
        [5] Sair\n'''))
        
            #Reconhecer Ação
        if acao == 1 :
            emprestar_livro()
        elif acao == 2 :
            listar_livros()
        elif acao == 3 :
            adicionar_livro()
        elif acao == 4 :
            devolver_livro()
        elif acao == 5 :
            sair()
usuario = input('Digite seu nome: ')      
mainMenu()   