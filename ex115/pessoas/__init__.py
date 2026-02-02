from ex115.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    print('-' * 30)
    print('MENU PRINCIPAL')
    print('-' * 30)
    print('1 - Cadastrar nova pessoa')
    print('2 - Listar pessoas cadastradas')
    print('3 - Sair do sistema')

    opcao = input('Sua opção: ').strip()

    if opcao == '1':
        print('-' * 30)
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
        print('Pessoa cadastrada com sucesso!')
        sleep(1)

    elif opcao == '2':
        listar(arq)
        sleep(2)

    elif opcao == '3':
        print('Saindo do sistema...')
        break

    else:
        print('Erro! Opção inválida.')
        sleep(1)