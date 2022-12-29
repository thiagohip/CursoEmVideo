def nota(* notas, sit=False):
    notes = {}
    max_nota = min_nota = notas[0] 
    for i in notas:
        if i > max_nota:
            max_nota = i
        if i < min_nota:
            min_nota = i
        avg = sum(notas)/len(notas)

        if avg >= 7:
            situ = 'Boa'
        elif avg < 7:
            situ = 'Razoável'
        elif avg <= 4:
            situ = 'Ruim'

    notes['total'] = len(notas)
    notes['maior'] = max_nota
    notes['menor'] = min_nota
    notes['média'] = avg
    if sit:
        notes['situação'] = situ
    return notes


resp = nota(3.3, 4.5, 7.8, 9.0, 5.2, sit=True)
print(resp)