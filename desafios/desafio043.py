print('-='*15)
print('CALCULADOR DE MASSA CORPORAL')
print('-='*15)

p = float(input('Digite o seu peso: '))
a = float(input('Digite a sua altura: '))

imc = p / (a*a)

print('O seu índice de massa corporal é de {}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você tem obesidade')
else:
    print('Você tem obesidade mórbida')
