def leiaDinheiro(msg):
    flag = False
    while not flag:
        inp = input(msg)
        inp = inp.replace(',', '.')
        if inp.isalpha():
            print(f'\033[0;31mERRO: \"{inp}\" é um valor inválido!\033[m')
        else:
            flag = True
            return float(inp)




