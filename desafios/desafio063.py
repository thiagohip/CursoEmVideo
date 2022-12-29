print('*-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('*-'*20)


n = int(input('Digite a quantidade de valores da sequência de Fibonacci que gostaria de ver: '))

i = 0
t1 = 0
t2 = 1


while i < n:
    print('{} → '.format(t1), end='')
    save = t1
    t1 = t2
    t2 = save+t2
    i += 1





#t1:0-1-2
#t2:1-2-


#Saida:0-1
