m = [[], [], []]
sump = 0
sum3 = 0
for i in range(3):
    for j in range(3):
        n = int(input('Digite um número: '))
        m[i].append(n)
        if n % 2 == 0:
            sump += n


print('=-'*20)
for i in range(3):
    for j in range(3):
        print(f'[ {m[i][j]} ]', end='')
    print(end='\n')
print('=-'*20)


for i in range(3):
    sum3 += m[i][2]

max2 = m[0][1]
for i in range(2):
    if m[i][1] > max2:
        max2 = m[i][1]

print(f'A soma de todos os pares é {sump}!')
print(f'A soma de todos os valores da 3ª coluna é {sum3}!')
print(f'O maior valor da segunda coluna é o {max2}!')



