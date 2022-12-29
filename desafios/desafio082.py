num = []

num.append(int(input('Digite um valor: ')))

while True:
    op = input('Quer continuar? [S/N] ')
    if op in 'NnSs':
        if op in 'Nn':
            break
        else:
            num.append(int(input('Digite um valor: ')))
    else:
        print('Opção inválida, tente novamente')

nump = []
numi = []

for i in num:
    if i % 2 == 0:
        nump.append(i)
    else:
        numi.append(i)

print('=-'*20)
print(f'A lista completa é {num}.')
print(f'A lista de pares é {nump}')
print(f'A lista de ímpares é {numi}')
