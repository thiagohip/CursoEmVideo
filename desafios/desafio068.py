from random import randint

v = 0


while True:
    npc = randint(0, 100)
    op = int(input('Escolha sua opção: [1] - Par [2] - Impar: '))
    n = int(input('Digite o valor: '))
    print(f'O valor escolhido pelo computador foi {npc}')
    if (n + npc) % 2 == 0:
        print('Deu par!')
        if op == 1:
            print('Você ganhou')
            v += 1
        elif op == 2:
            print('Você perdeu')
            break
    elif (n + npc) % 2 != 0:
        print('Deu impar!')
        if op == 1:
            print('Você perdeu')
            break
        elif op == 2:
            print('Você ganhou')
            v += 1

print(f'Você perdeu com {v} vitórias consecutivas')
