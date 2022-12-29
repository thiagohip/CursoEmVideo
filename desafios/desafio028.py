import random

random.seed()
n = int(random.random()*6)
print(n)
d = int(input("Tenten adivinha o número: "))

if n == d:
    print("Parabéns, você acertou o número!")
else:
    print("Você errou!")

