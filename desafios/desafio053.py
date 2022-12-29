flag = 1
f = input('Digite a frase: ')
f = f.replace(" ", "")
n = len(f)
inv = ''

for i in range(n-1,-1,-1):
    inv += f[i]


if inv == f:
    print('É um palíndrome')
else:
    print('Não é um palídrome')
