"""
Escrever um programa que leia n, e mostre os n primeiros números pares.
Exemplo:
Entrada: n = 5
Saída: 0 2 4 6 8
"""

cont = 1
n = int(input('Escreva a quantidades de números:'))
num = 0

while cont <= n:
    if num % 2 == 0:
        num += 2
    cont = cont + 1
    print(num)
    
