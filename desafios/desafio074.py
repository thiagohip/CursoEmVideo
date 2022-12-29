from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

maior = num[0]
menor = num[0]

for i in range(1, 5):
    if num[i] > maior:
        maior = num[i]
    elif num[i] < menor:
        menor = num[i]

print('Os números gerados foram:', end ='')
for i in num:
    print(f' {i} ', end='')

print('\n', f'Sendo o maior deles {maior} e o menor deles {menor}')


