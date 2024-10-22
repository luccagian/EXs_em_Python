"""
Preencha duas tuplas com 5 números cada, informados pelos usuários. Concatene as duas
tuplas e exiba a tupla resultante.
Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função
tuple.
tupla = tuple(lista) # converte lista em tupla
Exemplo: Suponha que as tuplas contenham os números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1)
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1)
"""

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
