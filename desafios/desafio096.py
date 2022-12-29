def area(l, c):
    a = l*c
    return a


print('Controle de Terrenos')
print('-'*30)

l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
print(f'A área de um terreno {l}x{c} é de {area(l, c)}m²')
