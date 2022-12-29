import moeda

valor = float(input('Digite o preço: R$'))

print(f'O dobro do valor é {moeda.dobro(valor)}')
print(f'{moeda.metade(valor)} é a metade desse valor.')
print(f'Aumento 10% é {moeda.aumentar(valor, 10)}')
print(f'Diminuido 30% ficamos com {moeda.diminuir(valor, 30)}')
