dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dia * 60) + (km * 0.15)
print('O total a ser pago é R${}'.format(pago))