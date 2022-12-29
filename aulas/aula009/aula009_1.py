
frase = 'Curso em video Python'


'Fatiamento'


'Por letra'
print(frase[9])

'Por espaço excluido o ultimo'
print(frase[9:14])

'Por espaço pulando por n'
print(frase[9:21:3])

'Começando de 0 até n ou n até maximo'
print(frase[:5])
print(frase[9:])





'Analises'

'Mostrar caracteres'
len(frase)

'Contar quantas letrar n tem'
frase.count('o')

'Quando apareceu n'
frase.find('deo')





'Transformação'

frase.replace('Python', 'Android')

frase.upper()
frase.lower()

print(frase.capitalize())
frase.title()

frase.strip()




'Divisão'

frase.split()
' '.join(frase)
