import operações

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor é {operações.dobro(valor,True)}')
print(f'{operações.metade(valor, True)} é a metade desse valor.')
print(f'Aumento 10% é {operações.aumentar(valor, 10,True)}')
print(f'Diminuido 30% ficamos com {operações.diminuir(valor, 30, True)}')
