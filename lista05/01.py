"""
Escreva um programa que leia 10 números e conte e mostre quantos são os números
negativos. Em seguida, o programa deve mostrar o maior número lido.
"""
neg = 0
numbma = 0
for n in range(10):
    numb = int(input(''))

    if numb < 0:
        neg += 1

    if numb > numbma:
        numbma = numb

print(numbma)
print(neg)
