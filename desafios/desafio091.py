from random import randint
from time import sleep
from operator import itemgetter

rs = {}

for i in range(4):
    rs[f'jogador{i + 1}'] = randint(1, 6)
    
for k, v in rs.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

ranking = list()
ranking = sorted(rs.items(), key=itemgetter(1), reverse=True)

print('-='*20)

for i in range(4):
    print(f'{i + 1}º lugar: {ranking[i][0]} com {ranking[i][1]}')
    






