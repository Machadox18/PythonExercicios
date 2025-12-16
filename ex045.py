from random import choice
from time import sleep
computador = choice(['pedra', 'papel', 'tesoura']) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vamos jogar pedra e papel e tesoura!')
print('-=-' * 20)
jogador = input('Jogue sua mão (pedra, papel ou tesoura): ').lower() # Jogador tenta adivinhar
print('Jokenpô')
if computador == 'pedra' and jogador == 'tesoura':
    print('Você perdeu!')
elif computador == 'papel' and jogador == 'pedra':
    print('Você perdeu!')
elif computador == 'tesoura' and jogador == 'papel':
    print('Você perdeu!')
elif jogador == computador:
    print('Empate!')
else:
    print('Você venceu!')

print(f'Computador jogou {computador}')

