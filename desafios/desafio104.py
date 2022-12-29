def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric:
            return n
        else:
            print('Digite um número inteiro!')


n = leiaInt('Digite um número')
print(f'Você digitou o número {n}')
        