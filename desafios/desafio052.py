flag = 0
n = int(input("Digite um número"))

for i in range(2,n-1):
    if(n % i == 0):
        flag+=1

if(flag == 0):
    print("O valor é primo")
else:
    print("Não é primo")
