s = ''
while s != 'M' and s != 'F':
    s = str(input('Qual é o seu sexo?: [M/F] ')).upper()
    if s != 'M' and s != 'F':
        print('Tente novamente.')
    if s == 'M':
        print('Você é do sexo masculino')
    elif s == 'F':
        print('Você é do sexo feminino')
print('Fim')