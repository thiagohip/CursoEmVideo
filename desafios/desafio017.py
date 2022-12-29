import math

cat_1 = int(input("Digite o valor de um dos catetos: "))
cat_2 = int(input("Digite o valor do outro cateto: "))

cat1_q = math.pow(cat_1, 2)
cat2_q = math.pow(cat_2, 2)
qhip = (cat2_q + cat1_q)
hip = math.sqrt(qhip)

print("A hipotenusa do triângulo com um cateto igual à {} cm e o outro cateto igual à {} cm, tem o valor de {} cm" .format(cat_1, cat_2, hip))
