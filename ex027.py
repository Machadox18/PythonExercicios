n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split() #ele vai fatiar/partir o nome em várias partes
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[len(nome)-1]))