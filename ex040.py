nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('APROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
