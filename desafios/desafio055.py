maior = menor = float(input('Digite um peso: '))

for i in range (0, 4):
    n = float(input('Digite outro peso: '))

    if n > maior:
        maior = n

    if n < menor:
        menor = n

print('O maior pesso foi {} e o menor foi {}'.format(maior, menor))
