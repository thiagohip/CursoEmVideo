num = []

for i in range(5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))

max_value = min_value = num[0]
max_pos = min_pos = 0


for i in range(5):
    if num[i] > max_value:
        max_value = num[i]
    elif num[i] < min_value:
        min_value = num[i]

for i in range(5):
    if num[i] == max_value:
        max_pos += 1
    elif num[i] == min_value:
        min_pos += 1

print('=-'*20 + '=')
print(f'Você digitou os valores {num}!')

if max_pos == 1:
    ind = 'na'
    poss = 'posição'
else:
    ind = 'nas'
    poss = 'posições'

print(f'O maior valor valor digitado foi {max_value} {ind} {poss}', end='')
for i, v in enumerate(num):
    if v == max_value:
        print(f' {i}...', end='')

if min_pos == 1:
    ind = 'na'
    poss = 'posição'
else:
    ind = 'nas'
    poss = 'posições'

print(f'\nO menor valor valor digitado foi {min_value} {ind} {poss}', end='')
for i, v in enumerate(num):
    if v == min_value:
        print(f' {i}...', end='')
