resp = 'S'
p = 0
maisdemil = 0
total = 0
menorpreco = 0
produtobarato = 0
while resp == 'S':
    p += 1
    print('----- {}ª PRODUTO -----'.format(p))
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: '))
    resp = str(input('Deseja continuar a comprar produtos? [S/N]')).strip().upper()
    total += preco
    if preco > 1000:
        maisdemil += 1
    if menorpreco == 0 or preco < menorpreco:
        menorpreco = preco
        produtobarato = nome
    if resp == 'N':
        print(f'Total gasto na compra: {total:.2f}')
        print(f'O produto mais barato foi {produtobarato}')
        print(f'Produtos que custaram mais de mil reais: {maisdemil}')
