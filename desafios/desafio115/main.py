from time import sleep

from lib import *

file = 'cadastros.txt'
if not fileExist(file):
    fileCreate(file)

op = menu()

while True:
    if op == 1:
        cadastro()
        sleep(2)
        op = menu()
    elif op == 2:
        cabeçalho('PESSOAS CADASTRADAS')
        fileView()
        sleep(2)
        op = menu()
    elif op == 3:
        cabeçalho('Saindo do sistema...')
        sleep(2)
        break
