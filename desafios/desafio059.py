flag = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while flag == 0:
    print('=-=' * 15)
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    op = int(input('>>>>> Qual a sua opção? '))

    if op == 1:
        print('A soma de {} e {} é {}.'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicado de {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('{} é o maior valor.'.format(n1))
        elif n2 > n1:
            print('{} é o maior valor.'.format(n2))
        else:
            print('Não tem valor maior, os dois são iguais')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        break
    else:
        print('Fail. Digite uma opção válida!')
