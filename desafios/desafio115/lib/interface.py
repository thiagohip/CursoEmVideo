from .fileManager import fileApp


def cor(cor, msg=''):
    return (f'\033[0;{cor}m{msg}\033[m')


def cabeçalho(msg):
    print('\033[0;33m-=\033[m' * 30)
    print(cor(34, msg).center(65))
    print('\033[0;33m-=\033[m' * 30)


def menu():

    cabeçalho('SISTEMA DE CADASTRO')
    print('\033[0;33m-=\033[m' * 30)
    print(f'{cor(33,"[1]")} {cor(34, "Cadastrar nova pessoa.")}'.center(40))
    print(f'{cor(33,"[2]")} {cor(34, "Ver pessoas cadastradas.")}'.center(40))
    print(f'{cor(33,"[3]")} {cor(34, "Sair do sistema.")}'.center(40))
    print('\033[0;33m-=\033[m' * 30)

    while True:
        try:
            op = int(input(f'{cor(34,"Escolha uma opção: ")}'))
        except Exception:
            print(cor(31, 'ERRO! Digite uma opção válida'))
        else:
            if op in (1, 2, 3):
                break
            else:
                print(cor(31, 'ERRO! Digite uma opção válida'))

    return op


def cadastro():

    cabeçalho('NOVO CADASTRO')

    while True:
        try:
            nm = str(input(cor(34, 'Nome: ')))
            age = int(input(cor(34, 'Idade: ')))
        except Exception:
            print(cor(31, 'ERRO! Tente novamente.'))
        else:
            break
    fileApp(nm, age)
    cabeçalho(f'Registro de {nm} feito com sucesso!')
