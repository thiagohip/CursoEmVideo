from datetime import datetime
pessoa = {}

pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano
carteira = int(input('Carteira de tabralho (Caso não tenha coloque 0): '))

if carteira != 0:
    pessoa['ctps'] = carteira
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))

print(f'O seu nome é {pessoa["nome"]}')
print(f'Você tem {pessoa["idade"]} anos de idade')

idade_start = pessoa['contratação'] - ano
pessoa['aposentadoria'] = idade_start + 35

if carteira == 0:
    print('Você não tem carteira de trabalho!')
else:
    print(f'Sua carteira de trabalho é de registro {pessoa["ctps"]}')
    print(f'O seu salaário é de R${pessoa["salario"]:.2f}')
    print(f'Você vai se aposentar com {pessoa["aposentadoria"]} anos de idade')
