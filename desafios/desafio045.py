from random import choice

print('-='*15)
print('JOKENPÔ')
print('-='*15)

escolhas = [1, 2, 3]
pc = choice(escolhas)

print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')

player = int(input('Escolhe sua opção: '))

if player == 1:
    if pc == 1:
        print('O pc escolher pedra!')
        print('Deu empate!')
    elif pc == 2:
        print('O pc escolheu papel!')
        print('Você perdeu!')
    elif pc == 3:
        print('O pc escolher tesoura')
        print('Você ganhou!')
elif player == 2:
    if pc == 1:
        print('O pc escolher pedra!')
        print('Você ganhou!')
    elif pc == 2:
        print('O pc escolheu papel!')
        print('Deu empate!')
    elif pc == 3:
        print('O pc escolher tesoura')
        print('Você perdeu!')
elif player == 3:
    if pc == 1:
        print('O pc escolher pedra!')
        print('Você perdeu!')
    elif pc == 2:
        print('O pc escolheu papel!')
        print('Você ganhou!')
    elif pc == 3:
        print('O pc escolher tesoura')
        print('Deu empate!')
