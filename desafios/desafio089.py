aluno = list()
nome = list()
notas = list()

while True:
    nm = str(input('Nome: '))
    nt1 = int(input('Nota 1: '))
    nt2 = int(input('Nota 2: '))
    notas.append(nt1)
    notas.append(nt2)
    nome.append(nm)
    nome.append(notas[:])
    notas.clear()
    aluno.append(nome[:])
    nome.clear()
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break

print('=-'*30)
print('No. NOME'+' '*8+'MÉDIA')
print('-'*20)
for i in range(len(aluno)):
    media = (aluno[i][1][0] + aluno[i][1][1]) / 2
    print(f'{i}  {aluno[i][0]} {media:>10}')

