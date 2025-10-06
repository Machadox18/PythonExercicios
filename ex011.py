altura = float(input('Digite a altura da sua parede em metros: '))
largura = float(input('Digite a largura da sua parede em metros: '))
soma = altura * largura
qnt = soma / 2
print('Para poder pintar a sua parede,será necessário {} litros de tinta'.format(qnt))