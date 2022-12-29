from datetime import date

atual = date.today().year
q = 0

for i in range(0, 7):
    a = int(input('Digite o ano de nascimento: '))
    if (atual - a) >= 18:
        q += 1

print('{} delas ja são maiores de idade'.format(q))
