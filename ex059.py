n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número:'))
s = 0
while s != 1 and s != 2 and s != 3 and s != 5:
    s = int(input('''O que você deseja fazer com estes números?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''))
    if s == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    if s == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
    if s == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n1 < n2:
            print('O maior número é {}'.format(n2))
        elif n1 == n2:
            print('Os números são iguais')
    if s == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número:'))
    if s == 5:
        print('Saindo do programa...')

