def leiaInt(msg):
    while True:
         valor = input(msg)
         if valor.isnumeric():
             return int(valor)
         else:
             print('Erro! Digite um numero inteiro válido.')


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')