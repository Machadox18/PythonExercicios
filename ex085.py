valores = []
numpar = list()
numimpar = list()
for c in range(0, 7):
    num = int(input('Digite um valor: '))
    valores.append(num)

    if num % 2 == 0:
        numpar.append(num)
    else:
        numimpar.append(num)
    valores.sort(reverse=True)
print(f'Valores pares digitados: {numpar}')
print(f'Valores impares digitados: {numimpar}')
print(f'Os valores em ordem crescente: {valores}')
