"""
Faça um programa que calcula e escreve a seguinte soma:
soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""

n = 0
soma = 0

for i in range(1,100,2):
    n += 1
    soma += i/n
print(soma)
