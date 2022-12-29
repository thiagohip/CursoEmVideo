h = int(input("Digite a altura da parede: "))
w = int(input("Digite a largura da parede: "))
a = int(h*w)
t = int(a/2)

print("Para pintar os {}m² de parede serão necessários {} baldes de tinta" .format(a, t))
