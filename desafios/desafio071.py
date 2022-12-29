print('='*20)
print('BANCO CEV')
print('='*20)

valor = int(input('Que valor você quer sacar? R$'))

while True:
    if valor > 50:
        print(f'Total de {valor//50} cédulas de R$50')
        valor = valor - (50*(valor//50))

    if valor > 20:
        print(f'Total de {valor // 20} cédulas de R$20')
        valor = valor - (20*(valor // 20))

    if valor > 10:
        print(f'Total de {valor // 10} cédulas de R$10')
        valor = valor - (10*(valor // 10))

    if valor > 1:
        print(f'Total de {valor // 1} cédulas de R$1')
        valor = valor - (valor // 1)

    if valor == 0:
        break
