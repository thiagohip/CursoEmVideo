num = []

n = int(input('Digite um valor: '))
num.append(n)
print('Número adicionado com sucesso!')
while True:
    op = input('Quer continuar? [S/N] ')
    if op in 'NnSs':
        break
    else:
        print('Opção inválida, tente novamente')

if op in 'Ss':
    while True:
        n = int(input('Digite um valor: '))
        flag = 0
        for i in range(len(num)):
            if n == num[i]:
                print('Número duplicado!')
                flag += 1
        if flag == 0:
            print('Número adicionado com sucesso! ')
            num.append(n)

        while True:

            op = input('Quer continuar? [S/N] ')
            if op in 'NnSs':
                break
            else:
                print('Opção inválida, tente novamente')

        if op in 'Nn':
            break
        elif op in 'Ss':
            continue

else:
    num.sort()
    print(f'Você digitou os valores {num}')

num.sort()
print(f'Você digitou os valores {num}')





