valorum = int(input('Digite um valor: '))
valordois = int(input('Digite outro valor: '))
if valorum > valordois:
    print('{} é maior que {}'.format(valorum, valordois))
elif valorum < valordois:
    print('{} é maior que {}'.format(valordois, valorum))
else:
    print('Não existe valor maior,os dois são iguais')