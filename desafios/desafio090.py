aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 6:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

print(f'O aluno(a) {aluno["nome"]} teve um média de {aluno["média"]}, então está {aluno["situação"]}thiago')
