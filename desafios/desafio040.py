n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

avg = (n1 + n2) / 2

if avg < 5:
    print('Reprovado')
elif avg > 7:
    print('Aprovado')
else:
    print('Recuperação')
    