valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        print(f'Todos os números digitados: {valores}')
        print(f'Todos os números pares digitados: {pares}')
        print(f'Todos os números impares digitados: {impares}')
        break