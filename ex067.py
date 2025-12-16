while True:
    num = int(input('Digite um número para ver sua tabuada:  '))
    if num < 0:
        break
    print('Programa tabuada encerrado,volte sempre')

    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num * c))

