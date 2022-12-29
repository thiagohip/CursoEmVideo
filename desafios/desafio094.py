pessoa = {}
galera = []

while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break

print(galera)

sumi = 0
for i in galera:
    sumi += i['idade']
avgi = int(sumi/len(galera))


print('=-'*20)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'A média de idade do grupo e de {avgi} anos de idade')
print(f'As mulheres do grupo são: ', end='')
for i in galera:
    if i['sexo'] in 'Ff':
        print(f'{i["nome"]}, ', end='')
print('')
print('As pessoas com idade acima da média são: ', end='')
for i in galera:
    if i['idade'] > avgi:
        print(f'{i["nome"]}, ')
