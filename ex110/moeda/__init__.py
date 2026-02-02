def metade(num):
    return num / 2

def dobro(num):
    return num * 2

def aumentar(num):
    return num * 1.80

def diminuir(num):
    return num * 0.65

def moeda(num):
    return f'R$ {num:.2f}'.replace('.', ',')


def resumo(num):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço:  {moeda(dobro(num))}')
    print(f'Metade do preço: {moeda(metade(num))}')
    print(f'80% de aumento:  {moeda(aumentar(num))}')
    print(f'35% de redução:  {moeda(diminuir(num))}')
    print('-'*30)