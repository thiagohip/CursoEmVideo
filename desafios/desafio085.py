num = [[], []]

for i in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print('=-'*20)
print(f'Os valores pares didigtado foram: {num[0]}')
print(f'Os valores ímpares digitado foram: {num[1]}')

