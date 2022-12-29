def contador(i, f, p):
    for j in range(i, f, p):
        print(f'{j} ', end='')
    print()

i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

contador(1, 11, 1)
contador(10, -1, -2)
contador(i, f, p)
