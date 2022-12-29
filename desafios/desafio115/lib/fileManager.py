

file = 'cadastros.txt'


def fileExist(file):
    try:
        fi = open(file, 'rt')
        fi.close()
    except Exception:
        return False
    else:
        return True


def fileCreate(file):
    try:
        with open(file, 'wt+'):
            print('Arquivo criado com sucesso')
    except Exception:
        print('Houve um erro na criação do arquivo')


def fileApp(nome, idade):
    with open(file, 'a') as arq:
        arq.write(f'{nome}' + '\n')
        arq.write(f'{idade}' + '\n')


def fileView():

    with open(file, 'r') as arq:
        lista = arq.readlines()

    for i in range(len(lista)):
        lista[i] = lista[i].replace('\n', '')

    for i in range(0, len(lista), 2):
        print(f'{lista[i]:<25}{lista[i + 1]:>25} anos')
