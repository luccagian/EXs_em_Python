"""
Faça um programa para gerar os n primeiros termos da seqüência:
            1 1 2 3 5 8 13 21 34 55 89 …
"""

n = int(input())
b = 1
c = 1

for i in range(n):
    if i <= 1:
        print('1')
    else:
        soma = b + c
        b = c
        c = soma 
        print(soma)
