valorproduto = float(input('Digite o valor do produto: '))
print('Possíveis formas de pagamento:')
print('A- A vista no dinheiro')
print('B- A vista no cartão')
print('C- Em até 2x no cartão')
print('D- 3x ou mais no cartão')
formadepaga = input('Qual será a forma de pagamento? Digite por favor ')
if formadepaga == 'A':
    desconto = valorproduto * 0.10
    valorfinal = valorproduto - desconto
    print('O valor do produto ficou um total de R${}'.format(valorfinal))
elif formadepaga == 'B':
    desconto = valorproduto * 0.05
    valorfinal = valorproduto - desconto
    print('O valor do produto ficou um total de R${}'.format(valorfinal))
elif formadepaga == 'C':
    print('O valor do produto ficou um total de R${}'.format(valorproduto))
elif formadepaga == 'D':
    juros = valorproduto * 0.20
    valorfinal = valorproduto + juros
    print('O valor do produto ficou um total de R${}'.format(valorfinal))
else:
    print('Forma de pagamento incorreta')