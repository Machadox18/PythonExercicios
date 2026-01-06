valores = []
contador = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    contador += 1
    print('Valor adicionado com sucesso!')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        valores.sort(reverse=True)
        print(f'O total de números digitados foi:{contador}')
        print('Lista ordenada:')
        print(valores)
    if resp == 'N' and 5 in valores:
        print('O valor 5 faz parte da lista!')
    elif resp == 'N' and not 5 in valores:
        print('O número 5 não está na lista!')

