lista1 = []
lista2 = []
lista3 = []

def intercala_numeros(lista1, lista2):
    for i in range(3):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3

for i in range(3):
    n = int(input(f'numero {i+1} da lista 1: '))
    lista1.append(n)
for i in range(3):
    n = int(input(f'numero {i+1} da lista 2: '))
    lista2.append(n)

p = intercala_numeros(lista1, lista2)

print(p)