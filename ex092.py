pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
pessoa['idade'] = int(input('Idade: '))
pessoa['ctps'] = int(input('Carteira de Trabalho(0 se não tiver): '))

if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + (65 - pessoa['idade'])

print('\n--- DADOS CADASTRADOS ---')
for k, v in pessoa.items():
    print(f'{k}: {v}')