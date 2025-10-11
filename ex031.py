dist = int(input('Qual a distancia da viagem? '))
if dist <= 200:
    print('O preço da passagem é R${}'.format(dist*0.50))
else:
    print('O preço da passagem é R${}'.format(dist*0.45))