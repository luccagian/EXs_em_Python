"""
Escreva um programa que leia 10 números inteiros. Para cada número lido, informe se
é par ou ímpar. Ao final, mostre o maior e o menor número lido.
"""

cont = 1


ma = 0
me = 0


while cont <= 10:
    num = int(input('Escreva um número:'))
    if cont == 1:
        ma == num and me == num
    cont = cont + 1
    if num > ma:
        ma = num
    if num <= me:
        me = num
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')
    if cont == 10:
        print(f'{ma} é o maior número, {me} é o menor número')
