vel = int(input("Qual a velocidade do veículo? "))
if vel > 80:
    multa = (vel-80)*7
    print("Estava acima do limite de velocidade! A multa é de R${}.00!".format(multa))
