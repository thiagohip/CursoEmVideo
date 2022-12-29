from math import factorial

def fat(num, show = False):
    """
    -> Faz o fatorial de um número
    fat(n, show=False)
    n: O número a ser calculado:
    show: Mostra ou não o processo de calculo
    return: O fatorial de n

    """

    if show:
        for i in range(num, 1, - 1):
            print(f'{i} x ', end='')
        print('1 = ', end='')
        return factorial(num)
    else:
        return factorial(num)

print(fat(12, True))
help(fat)    