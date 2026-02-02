from datetime import date

def voto(ano):
    idade = date.today().year - anonasc
    if idade >= 18 and idade < 70:
        print('VOTO OBRIGATÓRIO')
    elif idade >= 70:
        print('VOTO OPCIONAL')
    else:
        print('VOTO NEGADO')


anonasc = int(input('Digite o ano de nascimento: '))
voto(anonasc)
