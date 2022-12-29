n = int(input('Digite o valor para conversão: '))

print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

op = int(input("Digite a sua opção: "))

if op == 1:
    print('O valor {} em binário é {}'.format(n, bin(n).replace('0b', '')))
elif op == 2:
    print('O valor {} em octal é {}'.format(n, oct(n).replace('0o', '')))
elif op == 3:
    print('O valor {} em hexadecimal é {}' .format(n, hex(n).replace('0x', '')))
