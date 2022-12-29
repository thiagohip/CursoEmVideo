num = []
qtdnums = 5

for i in range(qtdnums):
    max_pos = i - 1
    min_pos = 0
    n = int(input(f'Digite um valor para a posição {i}: '))
    if i == 0:
        num.append(n)
        print('Adicionado a posição 0 da lista')
    else:
        for j in range(len(num)):
            if n < num[max_pos]:
                max_pos -= 1

            if n > num[min_pos]:
                min_pos += 1

        if min_pos == qtdnums - 1:
            print('Adicionado ao final da lista...')
        else:
            print(f'Adicionado a posição {min_pos} da lista...')

        num.insert(min_pos, n)

print(f'Os valores da lista em ordem é: {num}')