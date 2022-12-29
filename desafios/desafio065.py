print('*-'*20)
print('Média entre os valores')
print('*-'*20)

qtd = soma = i = 0



n = int(input('Digite o primeiro valor: '))
qtd += 1
soma += n
maior = menor = n

while i == 0:
    op = int(input('Quer continuar a digitar outros valores? [1] - Sim  [2] - Não: '))
    if op == 1:
        n = int(input('Digite outro valor: '))
        qtd += 1
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    elif op == 2:
        i += 1
    else:
        print('Opção inválida, tente novamente')


print(f'A média entre os valores digitador foi {(soma/qtd)}, o maior valor entre eles foi {maior} e o menor foi {menor}')
