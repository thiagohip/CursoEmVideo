from datetime import date

dtatual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
ano = dtatual-ano

if ano == 18:
    print('Já está na hora de se alistar')
elif ano > 18:
    print('Já passou {} ano(s) da hora de se alistar'.format(ano-18))
elif ano < 18:
    print('Ainda falta {} ano(s) para se alistar'.format(18-ano))
