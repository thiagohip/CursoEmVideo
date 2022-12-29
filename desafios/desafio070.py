print('='*25)
print('CARRINHO ONLINE')
print('='*25)

somac = prod1000 = 0
n = input('Digite o nome do produto: ')
p = float(input('Digite o preço do produto: '))
precb = p
prodb = n
somac += p
if p > 1000:
    prod1000 += 1

while True:
    print('=' * 25)
    op = input('Deseja adicionar mais produtos ao carrinho? [S/N]: ')
    print('=' * 25)
    if op in 'Nn':
        break
    elif op in 'Ss':
        n = input('Digite o nome do produto: ')
        p = float(input('Digite o preço do produto: '))

        somac += p
        if precb > p:
            prodb = n

        if p > 1000:
            prod1000 += 1

print('='*25)
print(f'A compra deu um total de R${somac}, tendo {prod1000} produtos com preço superior a R$1000.00 e sendo {prodb} o produto mais barato')




