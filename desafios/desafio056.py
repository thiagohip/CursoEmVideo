idade_homemmv = 0
soma_idades = 0
qtd_mulheresmv = 0

for i in range(0, 4):
    print('-----{}ªPessoa-----'.format(i + 1))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    if sexo == 'M':
        if idade > idade_homemmv:
            idade_homemmv = idade
            nome_homemmv = nome
    elif sexo == 'F':
        if idade < 20:
            qtd_mulheresmv+=1

    soma_idades += idade

print('A média de idade do grupo é de {} anos'.format(soma_idades / 4))
print('O homem mais velho tem {} anos e seu nome é {}'.format(idade_homemmv, nome_homemmv))
print('Ao todo são {} mulheres menores de 20 anos'.format(qtd_mulheresmv))
