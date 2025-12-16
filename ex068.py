from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()

    computador = randint(0, 10)
    total = jogador + computador

    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}')

    if total % 2 == 0:
        resultado = 'P'
        print('Deu PAR!')
    else:
        resultado = 'I'
        print('Deu ÍMPAR!')

    if escolha == resultado:
        print('Você VENCEU! Vamos jogar novamente...\n')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break

print('----- FIM DE JOGO -----')
print(f'Você venceu {vitorias} vezes consecutivas.')
