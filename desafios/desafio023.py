n = int(input("Digite um numero de 0 até 9999: "))

unidade = int(n%10)
dezena = int(((n%100)-unidade)/10)
centena = int((((n%1000)-dezena)-unidade)/100)
milhar = int(((((n%10000)-centena)-dezena)-unidade)/1000)

print("Unidade: " ,unidade)
print("Dezena: " ,dezena)
print("Centena: " ,centena)
print("Milhar: " ,milhar)
