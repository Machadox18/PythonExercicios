from random import randint
from time import sleep

jogos = []
quantidade = int(input('Quantos jogos você quer que eu sorteie?'))

print('\nGerando palpites...\n')

for i in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
        jogo.sort()
        jogos.append(jogo[:])

for i,jogo in enumerate(jogos):
    print(f'Jogo {i+1}: {jogo}')
    sleep(0.5)
print('\nBoa Sorte!')