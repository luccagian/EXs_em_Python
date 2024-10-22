"""
Faça um programa que leia um número n e imprima se ele é primo ou não. (um número
primo tem apenas 2 divisores: 1 e ele mesmo! O número 1 não é primo!!!)
"""

n = int(input())
a = 0

for i in range(2,n):
    if n % i == 0:
        print('não é primo')
        a += 1 
        break
if a == 0:
    print('é primo')
