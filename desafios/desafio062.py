pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))

print('O primeiro termo da razão é {}'.format(pt))
i = 0

while i < 1:
    op = int(input('Quantos mais termos quer mostrar?'))
    j = 0
    while j < op:
        pt += r
        print('{} - '.format(pt), end='')
        j += 1

    op = 0
