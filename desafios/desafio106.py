def ajuda(cmd):
    tam = len(cmd)
    print(f'\033[1;30;44m')
    print('~'* 35)
    print(f'Acessando o manual do comando {cmd}')
    print(('~'* 35), end='')
    print('\033[m')
    print(f'\033[1;30;107m')
    help(cmd)
    print('\033[m')

def título(msg, cor=47):
    tam = len(msg)
    print(f'\033[1;30;{cor}m')
    print('~'* tam)
    print(msg)
    print(('~'* tam), end='')
    print('\033[m')

while True:
    título('SISTEMA DE AJUDA PyHELP', 42)
    cmd = input('Função ou biblioteca -> ')
    if cmd in 'FIMfim':
        break
    else: 
        ajuda(cmd)

