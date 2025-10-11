frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira posição em que a letra A foi encontrada: {}'.format(frase.find('a')+1))
print('A última posição em que a letra A foi encontrada: {}'.format(frase.rfind('a')+1))