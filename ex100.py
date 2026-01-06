from random import randint
from time import sleep

numeros = []

def sorteia(lista):
    print('Sorteando 5 valores:' , end=' ')
    for _ in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somaPar(numeros)