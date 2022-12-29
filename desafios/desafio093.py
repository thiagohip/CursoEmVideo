jogador = {}
gols = []

jogador['nome'] = str(input('Nome do jogador: '))
qtdp = int(input(f'Quantas partida {jogador["nome"]} jogou? '))

for i in range(qtdp):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('=-'*20)
print(jogador)
print('=-'*20)

print(f'O nome do jogador é {jogador["nome"]}')
print('=-'*20)

print(f'O jogador {jogador["nome"]} jogou {qtdp} partidas')
for i in range(qtdp):
    print(f'   => Na partida {i + 1}, fez {jogador["gols"][i]} gols')