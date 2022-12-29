i = int(input('Informe a idade do atleta'))

if i < 10:
    print('A categoria do atleta é mirim')
elif i < 15:
    print('A categoria do atleta é infantil')
elif i < 20:
    print('A categoria do atleta é junior')
elif i == 20:
    print('A categoria do atleta é sênior')
else:
    print('A categoria do atleta é master')
