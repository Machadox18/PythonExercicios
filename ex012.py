num = float(input('Digite o preço aqui:'))
porcentagem = 5
resultado = num * porcentagem / 100
valorfinal = num - resultado
print('Com o desconto de {}%,o preço do seu produto fica:{}R$'.format(porcentagem, valorfinal))