m = [[], [], []]

for i in range(3):
    for j in range(3):
        n = int(input('Digite um número: '))
        m[i].append(n)


print('=-'*20)
for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]} ]', end='')


    print(end='\n')
