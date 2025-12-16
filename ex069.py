numhomem = 0
totmulher20 = 0
mais18 = 0
p = 0
resp = 'S'
while resp == 'S':
    p += 1
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        numhomem += 1
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if resp == 'N':
        print(f'Foram cadastradas {mais18} pessoas com mais de 18 anos.')
        print(f'Foi cadastrado o total de {numhomem} homens')
        print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
        break



