def maior(* val):
    m = val[0]
    cont = 0
    for i in val:
        cont += 1
        if i > m:
            m = i
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in val:
        print(f'{valor} ', end='')
    print(f'foram informados {cont} valores ao todo.')
    print(f'O maior valolr informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(20, 1, 6, 2)
    