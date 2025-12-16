from random import randint
from time import sleep
jogador = 0
contador = 0
computador = randint(0, 10) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while jogador != computador:
    jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
    contador += 1
    print('PROCESSANDO...')
    print('Errou,tente novamente.')
    if jogador == computador:
        print('PARABÉNS! Você precisou de {} tentativas para me vencer.'.format(contador))
