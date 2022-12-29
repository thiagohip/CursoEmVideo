time = ('Palmeiras', 'Inter', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Chapecoense')

#print('Os cinco primeiros times colocados no brasilerão foram:')
#for i in range(0, 5):
#    print(time[i])

#print('Os cinco últimos times colocados no brasilerão foram:')
#for i in range(-1, -6, -1):
#    print(time[i])

#print(sorted(time))

cha = time.index('Chapecoense')+1
print(f'O time da chapecoense está na {cha}º posição na tabela')