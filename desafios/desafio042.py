print('-='*20)
print('ANALISADOR DE TRIÂNGULOS 2.0')
print('-='*20)

l1 = int(input('Informe o primeiro lado do triângulo: '))
l2 = int(input('Informe o segundo lado do triângulo: '))
l3 = int(input('Informe o terceiro lado do triângulo: '))

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    if l1 == l2 == l3:
        print('Esses segmentos formam um triangulo equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Esses segmentos formam um triângulo isósceles')
    elif l1 != l2 != l3:
        print('Esses segmentos formam um triângulo escaleno')
else:
    print('Esses segmentos não formam um triângulo!')
