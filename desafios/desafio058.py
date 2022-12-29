from random import random

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')

n = int(10 * random())

i = 0
while i == 0:
    att = int(input('Qual o seu palpite? '))
    if att > n:
        print('Menos... Tente outra vez.')
    elif att < n:
        print('Mais... Tente outra vez')
    else:
        print('Parabéns, você acertou o número')
        i += 1



