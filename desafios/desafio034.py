s = int(input("Digite o valor do salário: "))

if(s > 1250):
    s2 = s+s*0.1
else:
    s2 = s+s*0.15

print("O novo salário é de R${}".format(s2))

