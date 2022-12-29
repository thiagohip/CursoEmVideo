flag = 0
sexo = str(input('Informe seu sexo: [M/F] ').strip())

while flag == 0:
    if sexo in 'MmFf':
        flag += 1
    else:
        sexo = str(input('Dados, inválidos. Por favor, informe seu sexo: ').strip())

print('Sexo {} registrado com sucesso'.format(sexo.upper()))
