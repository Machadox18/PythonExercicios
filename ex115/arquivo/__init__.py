def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    a = open(nome, 'wt+')
    a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    a = open(arquivo, 'at')
    a.write(f'{nome};{idade}\n')
    a.close()


def listar(arquivo):
    a = open(arquivo, 'rt')
    print('-' * 30)
    print(f'{"NOME":<20}IDADE')
    print('-' * 30)
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<20}{dado[1]}')
    a.close()