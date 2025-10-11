salario = float(input('Digite o seu salario: '))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print('O seu salário com o aumento foi {}'.format(salario))
else:
    salario = salario + (salario * 15 / 100)
    print('O seu salário com o aumento foi {}'.format(salario))