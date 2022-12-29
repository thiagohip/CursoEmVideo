from datetime import date

def voto(a):
    if a >= 65:
        ob = 'VOTO OPCIONAL'
    elif a >= 18:
        ob = 'VOTO OBRIGATÓRIO'
    else:
        ob = 'AINDA NÃO PODE VOTAR'
    return ob

print('-='*30)
ano_born = int(input('Qual o seu ano de nascimento? '))
ano_now = date.today().year
age = ano_now - ano_born
print(f'Com {age} anos: {voto(age)}')


    
