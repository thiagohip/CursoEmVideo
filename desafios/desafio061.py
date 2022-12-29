pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))

i = 0

while i < 10:
    print('{} - '.format(pt), end='')
    pt += r
    i += 1

print('Fim')
