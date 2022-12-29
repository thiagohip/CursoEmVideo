i = soma = 0


n = int(input('Vamos digitar vários números, digite 999 para parar: '))
maior = n

if n == 999:
    print('Mas já?')
    i += 1


while i == 0:
    soma += n
    if n > maior:
        maior = n
    n = int(input('Digite outro valor: '))
    if n == 999:
        i += 1
        print('O maior valor digitado foi {} e a soma entre eles foi {}'.format(maior, soma))

