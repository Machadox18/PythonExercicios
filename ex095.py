jogadores = []

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = input('Nome do jogador: ').strip()
    total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(total_partidas):
        gols = int(input(f'   Quantos gols na partida {i + 1}? '))
        partidas.append(gols)

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    jogadores.append(jogador.copy())

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Erro! Quer continuar? [S/N]: ').strip().upper()[0]

    if continuar == 'N':
        break

# ---- TABELA RESUMO ----
print('\n' + '-=' * 30)
print(f'{"cod":<5}{"nome":<15}{"gols":<20}{"total":<5}')
print('-' * 45)

for i, j in enumerate(jogadores):
    print(f'{i:<5}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')

# ---- DETALHES DO JOGADOR ----
while True:
    print('-' * 45)
    busca = int(input('Mostrar dados de qual jogador? (999 para sair): '))

    if busca == 999:
        print('Encerrando...')
        break

    if busca >= len(jogadores):
        print('Erro! Jogador não existe.')
    else:
        print(f'-- Levantamento do jogador {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i + 1} fez {g} gols')