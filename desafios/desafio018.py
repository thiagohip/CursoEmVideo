import math

d = float(input(("Digite o valor do ângulo em graus:")))
dr = math.radians(d)
dsin = math.sin(dr)
dcos = math.cos(dr)

print("O ângulo de {}º tem um cosseno de {} e um seno de {}".format(d,dcos,dsin))
