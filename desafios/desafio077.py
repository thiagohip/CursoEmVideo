word = ('APRENDE', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in word:
    print(f'\nNa palvara {i} temos: ', end = '')
    for letra in i:
        if letra in 'AEIOU':
            print(letra, end = '')