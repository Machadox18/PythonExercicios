def notas(*n, sit=True):


    resultado = {}

    resultado['total'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['media'] = sum(n) / len(n)

    if sit:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado['situacao'] = 'RUIM'

    return resultado


resp = notas(5.5, 2.5, 8, 6.5, sit=True)
print(resp)