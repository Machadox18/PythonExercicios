jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = float(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = float(input('Quantos gols ele tem na carreira? '))

aproveitamento = jogador['gols'] / jogador['partidas']
print(f'{jogador["nome"]} tem uma média de {aproveitamento:.2f} gols por partida.')
