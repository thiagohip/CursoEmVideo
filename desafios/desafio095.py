jogador = {}
gols = []
jogadores = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    qtdp = int(input(f'Quantas partida {jogador["nome"]} jogou? '))

    for i in range(qtdp):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear
    gols.clear

    while True:
        op = str(input('Quer continuar? [S/N] '))
        if op in 'SsNn':
            if op in 'NnSs':
                break
        else:
            print('Opção inválida tente novamente')
    if op in 'Nn':
        break

print(jogadores)

print('-='*30)
print('cod  nome        gols        total')
print('-'*20)
for i in range(len(jogadores)):
    print(f'{i} {jogadores[i]["nome"]}      {jogadores[i]["gols"]}      {jogadores[i]["total"]}')
print('-'*20)
j = int(input('Mostrar dado de qual jogador? '))
print(f' --LEVANTAMENTO DO JOGADOR {jogadores[j]["nome"].upper()}')

for i in range(len(jogadores[j]['gols'])):
    print(f'No jogo {i + 1} fez {jogadores[j]["gols"][i]} gols')
