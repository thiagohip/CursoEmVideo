def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Esse usuário não quis informar o valor!\033[m')
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real!\033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Esse usuário não quis informar o valor!\033[m')
        else:
            break
    return n



numInt = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {numInt} e o número real')
