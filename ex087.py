matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# Leitura dos valores
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(
            input(f"Digite um valor para [{linha}, {coluna}]: ")
        )

        # Soma dos pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

# Soma da terceira coluna
for linha in range(3):
    soma_terceira_coluna += matriz[linha][2]

# Maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

print("-=" * 25)

# Exibição da matriz
for linha in range(3):
    for coluna in range(3):
        print(f"[ {matriz[linha][coluna]:^5} ]", end="")
    print()

print("-=" * 25)
print(f"A soma dos valores pares é: {soma_pares}")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_segunda_linha}")