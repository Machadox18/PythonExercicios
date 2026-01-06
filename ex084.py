dados = []
maior = menor = 0
while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))

    dados.append([nome, peso])

    if len(dados) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        print(f'Ao todo, foram cadastrado {len(dados)} pessoas.')
        print(f'O maior peso foi de {maior}Kg e o menor peso foi de {menor}Kg.')
        break