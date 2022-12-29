import operações

valor = float(input('Digite um valor: R$'))

print(f'O dobro do valor é {operações.moeda(operações.dobro(valor))}')
print(f'{operações.moeda(operações.metade(valor))} é a metade desse valor.')
print(f'Aumento 10% é {operações.moeda(operações.aumentar(valor, 10))}')
print(f'Diminuido 30% ficamos com {operações.moeda(operações.diminuir(valor, 30))}')
