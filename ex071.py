valor = int(input('Qual valor você quer sacar? R$: '))

ced50 = ced20 = ced10 =ced1 = 0

while valor > 0:
    if valor >= 50:
        valor -= 50
        ced50 += 1
    elif valor >= 20:
        valor -= 20
        ced20 += 1
    elif valor >= 10:
        valor -= 10
        ced10 += 1
    else:
        valor -= 1
        ced1 += 1

print('----- CÉDULAS ENTREGUES -----')
if ced50 > 0:
    print(f'{ced50} cédulas de R$50')
if ced20 > 0:
    print(f'{ced20} cédulas de R$20')
if ced10 > 0:
    print(f'{ced10} cédulas de R$10')
if ced1 > 0:
    print(f'{ced1} cédulas de R$1')