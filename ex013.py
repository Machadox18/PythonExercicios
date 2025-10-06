sal = float(input('Digite o seu salário aqui:R$'))
aumento = 15
novo_preco = sal + (sal * (aumento / 100))
print('O seu novo salário é R${:.2f}'.format(novo_preco))

