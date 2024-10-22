"""
Escrever um programa que leia n, e mostre todas as potências de 2 menores que n.
Exemplo:
Entrada: n = 100
Saída: 1 2 4 8 16 32 64
"""

n = int(input('Digite o número aqui:')) 
nump = 1

n -=1

while nump < n:
    nump = nump*2

    print(nump)
