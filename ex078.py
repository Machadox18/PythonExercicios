valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} e ele se encontra na posição {valores.index(maior)}.')
print(f'O menor valor digitado foi {menor} e ele se encontra na posição {valores.index(menor)}.')