km = int(input("Quantos Km foram percorridos com o carros? "))
d = int(input("Por quantos dias o carros foi alugado?"))

t = (km*0.15) + (d*60)

print("O valor a se pagar pelo aluguel do carro é de R${:.2f}".format(t))
