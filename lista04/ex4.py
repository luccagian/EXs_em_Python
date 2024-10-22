"""
Escrever um programa que leia n, e mostre os quadrados menores que n.
Exemplo:
Entrada: n = 100
Saída: 0 1 4 9 16 25 36 49 64 81
"""
n = int(input('Digite o número aqui:')) 
numq = 0
num = 0

while n > numq:
    numq = num**2
    num += 1
    print(numq)
