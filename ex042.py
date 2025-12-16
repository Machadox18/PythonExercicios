a = float(input('Digite o tamanho da primeira reta do triângulo: '))
b = float(input('Digite o tamanho da segunda reta do triângulo: '))
c = float(input('Digite o tamanho da terceira reta do triângulo: ')) 
if a == b == c:
    print('Este é um triângulo equilátero')
elif a == b or a == c or b == c:
    print('Este é um triângulo isósceles')
elif a != b !=c or a != c:
    print('Este é um triângulo escaleno')
else:
    print('Não é possível montar um triângulo.')