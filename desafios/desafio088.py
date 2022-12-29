from random import randint
from time import sleep

qtdj = int(input('Quantos jogos serão gerados? '))

ms = list()
jogo = list()

for i in range(qtdj):
    k = 0
    flag = 0
    while k < 6:
        n = randint(1, 60)
        for l in jogo:
            if n == l:
                flag += 1

        if flag == 0:
            jogo.append(n)
            k += 1
    jogo.sort()
    ms.append(jogo[:])
    jogo.clear()

print(f'-=-=-=- SORTEANDO {qtdj} JOGOS -=-=-=-')
for i in range(qtdj):
    sleep(0.5)
    print(f'Jogo {i+1}: {ms[i]}')
print(f'-=-=-=- BOA SORTE -=-=-=-')
