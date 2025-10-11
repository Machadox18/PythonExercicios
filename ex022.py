name = str(input('Digite seu nome completo: ')).strip() #elimina os espaços antes e depois
print('Seu nome em Maiúsculas é {}'.format(name.upper()))
print('Seu nome em Minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {} letras'.format(name.find(' ')))