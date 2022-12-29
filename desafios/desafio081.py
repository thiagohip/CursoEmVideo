num = []

num.append(int(input('Digite um valor: ')))

while True:
    op = input('Quer continuar? [S/N] ')
    if op in 'NnSs':
        if op in 'Nn':
            break
        else:
            num.append(int(input('Digite um valor: ')))
    else:
        print('Opção inválida, tente novamente')



print('=-'*30)

num.sort(reverse=True)
print(f'Você digitou {len(num)} elementos')
print(f'Os valores em ordem descrescente são {num}')
if 5 in num:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')