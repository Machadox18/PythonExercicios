vel = float(input('Qual a velocidade atual em km do seu carro? '))
if vel > 80:
    print('Você foi multado em R$ {:.2f}'.format((vel - 80) * 7))
else:
    print('Continue dirigindo com segurança!')