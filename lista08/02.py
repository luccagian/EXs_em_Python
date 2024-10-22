lista1 = []
lista = []

for i in range(5):
    n = int(input(f'Numero {i+1} da tupla 1: '))
    lista.append(n)

for i in range(5):
    n = int(input(f'Numero {i+1} da tupla 2: '))
    lista1.append(n)

tupla1 = tuple(lista)
tupla2 = tuple(lista1)

tupla3 = tupla1 + tupla2

print(tupla3)