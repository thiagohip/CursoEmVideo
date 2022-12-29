dis = int(input("Qual a distâcia da viagem? "))

if dis > 200:
    passagem = dis*0.5
else:
    passagem = dis*0.45

print("O preço da passagem é de R${}".format(passagem))
