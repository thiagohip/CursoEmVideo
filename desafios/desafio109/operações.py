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



