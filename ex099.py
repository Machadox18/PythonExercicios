def maior(*numeros):
    print('-=' * 20)

    if len(numeros) == 0:
        print('Nenhum valor foi informado.')
        return

    print('Analisando os valores passados...')
    for n in numeros:
        print(n, end=' ')

    print(f'\nO maior valor informado foi {max(numeros)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()