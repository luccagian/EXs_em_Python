"""
Escreva uma função que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
Categoria Idade
Infantil A    5 a 7
Infantil B    8 a 10
Juvenil A     11 a 13
Juvenil B     14 a 17
Sênior maiores de 18 anos
"""

def gp(id):
    if id >= 5 and id <= 7:
        cat = 'infantil A'
    elif id >= 8 and id <= 10:
        cat = 'infantil B'
    elif id >= 11 and id <= 13:
        cat = 'juvenil A'
    elif id >= 14 and id <= 17:
        cat = 'juvenil B'
    elif id > 18:
        cat = 'senior'
    return cat

id = int(input())

tabela = gp(id)

print(tabela)
