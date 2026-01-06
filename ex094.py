pessoas = []
soma_idade = 0

while True:
    pessoa = {}

    pessoa['nome'] = input('Nome: ').strip()
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Erro! Sexo [M/F]: ').strip().upper()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']

    pessoas.append(pessoa.copy())

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Erro! Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

# ---- RESULTADOS ----
qnt_pessoas = len(pessoas)
media_idade = soma_idade / qnt_pessoas

print('-=' * 30)
print(f'A) Foram cadastradas {qnt_pessoas} pessoas')
print(f'B) A média de idade é {media_idade:.2f}')

print('C) Mulheres cadastradas:', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()

print('D) Pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'   nome = {p["nome"]}; idade = {p["idade"]}')
