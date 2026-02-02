from ex111.utilidadescev import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(',', '.')

        if entrada.replace('.', '').isdigit():
            return float(entrada)
        else:
            print(f'Erro! "{entrada}" é um preço inválido.')

def resumo(num):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: {moeda.moeda(num)}')
    print(f'Dobro do preço:  {moeda.moeda(moeda.dobro(num))}')
    print(f'Metade do preço: {moeda.moeda(moeda.metade(num))}')
    print(f'80% de aumento:  {moeda.moeda(moeda.aumentar(num))}')
    print(f'35% de redução:  {moeda.moeda(moeda.diminuir(num))}')
    print('-'*30)