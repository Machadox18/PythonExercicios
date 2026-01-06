boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['média'] = int(input(f'Média de {boletim["nome"]}: '))
print(f'Nome é igual a {boletim["nome"]}')
print(f'Média é igual a {boletim["média"]}')

if boletim["média"] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')