n = int(input('Digite o valor para calcular seu fatorial: '))
fat = 1

for i in range (n, 1, -1):
    fat = fat*i

print('O fatorial de {} é {}'.format(n, fat))
