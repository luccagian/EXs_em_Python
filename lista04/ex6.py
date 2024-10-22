"""
Escreva um programa que calcule a soma de todos os números pares entre 2 e 100
(inclusive)
"""

n = 0
soma = 0 

while n < 100:
    n += 1 
    if n % 2 == 0:
        soma = soma + n
        print(soma)
