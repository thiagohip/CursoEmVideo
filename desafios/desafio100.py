from random import randint
from time import sleep

def sorteia():
    for i in range(5):
        n = randint(1, 10)
        num.append(n)
    print('-='*25)
    for i in num:
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('foram os números sorteados da lista')

def somaPar(num):
    sumPar = 0
    for i in range(len(num)):
        if num[i] % 2 == 0:
            sumPar += num[i]
    print('-='*25)
    print(f'A soma de todos os valores pares da lista foi {sumPar}')


num = list()
sorteia()
somaPar(num)
