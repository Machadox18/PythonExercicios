def titulo(msg):
    print('\033[1;44m~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print('\033[m', end='')


def ajuda(comando):
    print('\033[7;40m', end='')
    help(comando)
    print('\033[m', end='')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = input('\033[1;32mFunção ou Biblioteca > \033[m').strip()

    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!')
