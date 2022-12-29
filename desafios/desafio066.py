i = soma = qtd = 0


n = int(input('Vamos digitar vários números, digite 999 para parar: '))

if n == 999:
    print('Mas já?')
    i += 1

if i == 0:
    while True:
        soma += n
        qtd += 1
        n = int(input('Digite outro valor: '))
        if n == 999:
            print(f'Foram {qtd} valores digitador e a soma entre eles foi {soma}')
            break


