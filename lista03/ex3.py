"""
Escreva um programa que leia três números inteiros, em seguida determine e mostre o
maior deles.
"""
n1 = int(input('Digite 1 numero:'))
n2 = int(input('Digite 2 numero:'))
n3 = int(input('Digite 3 numero:'))

if n1 > n2 and n1 > n3:
    print(f'o maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'o maior número é {n2}')
elif n3 > n2 and n3 > n1:
    print(f'o maior número é {n3}')
