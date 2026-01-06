valores = []

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

    valores.sort()
    print('Os valores únicos digitados em oredem crescente são:')
    print(valores)