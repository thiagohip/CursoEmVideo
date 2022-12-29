exp = input('Digite um expressão: ')
exp = exp.replace(' ', '')
qtd = 0
flag = 0

for i in range(len(exp)):
    if exp[i] == '(':
        qtd += 1
    elif exp[i] == ')':
        qtd -= 1

    if qtd < 0:
        flag += 1

if flag > 0:
    print('A expressão está errada')
else:
    print('A expressão está correta')

