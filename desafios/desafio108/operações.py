def aumentar(n, pc):
    valor = n + ((n/100)*pc)
    return valor

def diminuir(n, pc):
    valor = n - ((n/100)*pc)
    return valor

def dobro(n):
    return n*2

def metade(n):
    return n/2

def moeda(valor):
    value = str(f'R${valor:.2f}')
    value = value.replace('.', ',')
    return value

