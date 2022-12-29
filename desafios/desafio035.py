l1 = int(input('Informe o primeiro lado do triângulo'))
l2 = int(input('Informe o segundo lado do triângulo'))
l3 = int(input('Informe o terceiro lado do triângulo'))

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print('Podem formar um triângulo')
else:
    print('Não formam um triângulo')
