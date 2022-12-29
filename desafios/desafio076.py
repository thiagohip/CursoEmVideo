produtos = (
    'Pão', 1,
    'Leite', 5,
    'Biscoito', 1.5,
    'Salgado', 5,
    'Cachaça', 3,
    'Refrigerante', 6,
)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end = '')
    else:
        print(f'R${produtos[i]:>3.2f}')