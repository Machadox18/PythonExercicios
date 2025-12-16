n = soma = 0
while True:
    n =int(input('Digite um número: [999 para parar]'))
    if n == 999:
       break
    soma += n
    totaldigi = n + 1 - 1
print(f'O total de números digitados é {totaldigi}')
print(f'A soma dos números digitados é igual a {soma}')