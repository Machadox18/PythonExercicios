a = float(input('Digite o tamanho da primeira reta do triângulo: '))
b = float(input('Digite o tamanho da segunda reta do triângulo: '))
c = float(input('Digite o tamanho da terceira reta do triângulo: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível montar um triângulo!')
else:
    print('Não é possível montar um triângulo.')