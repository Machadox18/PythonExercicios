def fatorial(n, show=False):
    """
    ->Calcula o fatorial de um numero
    :param n:número a ser calculado
    :param show: (opcional) mostra ou não o processo do cálculo
    :return: o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
print(fatorial(4))