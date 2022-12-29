
pessoas = list()
pessoa = list()

nome = str(input('Nome: '))
peso = str(input('Peso: '))
pessoa.append(nome)
pessoa.append(peso)
pessoas.append(pessoa[:])
pessoa.clear()


maxp = minp = peso

op = str(input('Quer continuar? [S/N] '))
if op in 'Ss':
     while True:
        pessoa.append(str(input('Nome: ')))
        pessoa.append(str(input('Peso: ')))
        pessoas.append(pessoa[:])
        pessoa.clear()
        op = str(input('Quer continuar? [S/N] '))
        if op in 'Nn':
            break

qtdp = len(pessoas)

for i in range(qtdp):

    if pessoas[i][1] > maxp:
        maxp = pessoas[i][1]

    if pessoas[i][1] < minp:
        minp = pessoas[i][1]

print(f'Foram cadastradas {qtdp} pessoas')

print('As pessoas mais magras são: ', end = '')
for i in range(qtdp):
    if pessoas[i][1] == minp:
        print(' - ' + pessoas[i][0], end = '')

print('\nAs pessoas mais gordas são: ', end = '')
for i in range(qtdp):
    if pessoas[i][1] == maxp:
        print(' - ' + pessoas[i][0], end = '')





