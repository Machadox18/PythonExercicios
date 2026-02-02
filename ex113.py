def leiaInt(msg):
    while True:
         valor = input(msg)
         if valor.isnumeric():
             return int(valor)
         else:
             print('ERRO! Digite um numero inteiro válido.')

def leiaFloat(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return float(valor)
        else:
            print('ERRO!Digite um número real válido.')


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')