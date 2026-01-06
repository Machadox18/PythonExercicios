numeros = (
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: '))
)
print('Você digitou os valores:', numeros)

# A) Quantas vezes aparece o número 9
print(f'O número 9 apareceu {numeros.count(9)} vezes')

# B) Posição do primeiro número 3
if 3 in numeros:
    print(f'O número 3 apareceu pela primeira vez na posição {numeros.index(3) + 1}')
else:
    print('O número 3 não foi digitado')

# C) Números pares
print('Os números pares digitados foram:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')