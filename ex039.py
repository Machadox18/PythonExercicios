from datetime import date

anonascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - anonascimento
tempoalistar = 18 - idade
if idade < 18:
    print('Você tem {} anos.'.format(idade))
    print('Você ainda vai se alistar,falta {} anos'.format(tempoalistar))
elif idade == 18:
    print('Você tem {} anos.'.format(idade))
    print('Está na hora de se alistar')
elif idade > 18:
    print('Você tem {} anos.'.format(idade))
    print('Já passou do tempo de alistamento')