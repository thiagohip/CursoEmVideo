def ficha(nm='', gols=0):
    if nm == '':
        nm = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f'O jogador {nm} fez {gols} no campeonato')    

nm = input('Nome do jogador: ')
gols = input('Número de gols: ')
ficha(nm, gols)