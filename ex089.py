boletim = []

for c in range(0, 2):
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome,[nota1, nota2], media])

print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
for i, aluno in enumerate(boletim):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

print("-=" * 30)

# Consulta individual
while True:
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print("Finalizando...")
        break
    if opcao < len(boletim):
        print(f"Notas de {boletim[opcao][0]} são {boletim[opcao][1]}")
    else:
        print("Opção inválida!")