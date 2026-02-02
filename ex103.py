def ficha(nome = '<desconhecido>', gols=0):
    """
    -> Mostra a ficha de um jogador.
    :param nome: nome do jogador (opcional)
    :param gols: número de gols feitos (opcional)
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = input('Nome do jogador: ').strip()
g = input('Nome do gols: ').strip()

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols = g)
else:
    ficha(n, g)