qtdp = qtdh = qtdm20 = 0


while True:
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo [M/F]: ')
    qtdp += 1
    if s in 'Mm':
        qtdh += 1
    elif s in 'Ff':
        if i < 20:
            qtdm20 += 1
    op = input('Quer adicionar mais pessoas? [S/N]: ')
    if op in 'Nn':
        break

print(f'Das {qtdp} pessoas adicionada, são {qtdh}  homens e {qtdm20} mulheres com idades menores de 20 anos')


