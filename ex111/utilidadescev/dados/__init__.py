from ex112 import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(',', '.')

        if entrada.replace('.', '').isdigit():
            return float(entrada)
        else:
            print(f'Erro! "{entrada}" é um preço inválido.')
