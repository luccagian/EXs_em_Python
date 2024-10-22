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