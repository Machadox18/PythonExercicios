valorcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
qntanos = float(input('Quantos anos de financiamento? '))
prestação = valorcasa / (qntanos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorcasa, qntanos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo NEGADO!')
