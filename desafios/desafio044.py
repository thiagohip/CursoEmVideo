print('-='*15)
print('CALCULADOR DE DESCONTOS')
print('-='*15)

valor = int(input('Digite o valor da compra: '))

print('[1] - A vista, dinheiro/cheque: 10% de desconto')
print('[2] - A vista, cartão: 5% de desconto')
print('[3] - Até 2x no cartão sem juros')
print('[4] - Parcelamento com juros: 20% de juros')

op = int(input('Escolhe sua opção: '))

if op == 1:
    print('O valor será de R${}'.format(valor * 0.9))
elif op == 2:
    print('O valor será de R${}'.format(valor * 0.95))
elif op == 3:
    print('O valor será de R${}'.format(valor))
elif op == 4:
    print('O valor será de R${}'.format(valor * 1.20))
