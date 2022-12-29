vc = int(input('Informa o valor da casa: '))
s = int(input('Informa seu salaário mensal: '))
p = int(input('Informe em quantas parcelas pretende financiar esta casa: '))

if (vc / p) > (s * 0.3):
    print('Infelizmente seu financiamento não será aceito!')
else:
    print('O seu financiamento será aceito!')
