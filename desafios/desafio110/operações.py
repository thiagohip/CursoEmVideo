def moeda(valor):
    value = str(f'R${valor:.2f}')
    value = value.replace('.', ',')
    return value

def aumentar(n=0, pc=0, f=False):
    valor = n + ((n/100)*pc)
    if f:
        valor = moeda(valor)
        return valor
    else:
        return valor

def diminuir(n=0, pc=0, f=False):
    valor = n - ((n/100)*pc)
    if f:
        valor = moeda(valor)
        return valor
    else:
        return valor

def dobro(n=0, f=False):
    valor = n*2
    if f:
        return moeda(valor)
    else:
        return valor

def metade(n, f=False):
    valor = n/2
    if f:
        return moeda(valor)
    else:
        return valor

def resumo(value, pUp, pDwn):
    print('-='*20)
    print('RESUMO DO VALOR'.center(40))
    print('-='*20)
    print(f'Preço analisado: \t{moeda(value)}')
    print(f'Dobro do preço: \t{dobro(value, True)}')
    print(f'Metade do preço: \t{metade(value, True)}')
    print(f'{pUp}% de aumento: \t{aumentar(value, pUp, True)}')
    print(f'{pDwn}% de redução: \t{diminuir(value, pDwn, True)}')
    print('-='*20)


