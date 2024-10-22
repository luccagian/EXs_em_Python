"""
Escrever um programa que lê um valor em reais e calcule qual o menor número
possível de notas de 100, 50, 10, 5 e 1 em que o valor lido pode ser decomposto. Escrever
o valor lido e a relação de notas necessárias.
Por exemplo: valor = R$ 238,00
notas de 100: 2
notas de 50: 0
notas de 10: 3
notas de 5: 1
notas de 1: 3
"""

valor = int(input('Digite o valor:'))

nota100 = 0
nota50 = 0
nota10 = 0 
nota5 = 0 
nota1 = 0

if (valor // 100) >= 0:
    nota100 = valor // 100
    valor = valor % 100
if (valor // 50) >= 0:
    nota50 = valor // 50
    valor = valor % 50

if (valor // 10) >= 0:
    nota10 = valor // 10
    valor = valor % 10

if (valor // 5) >= 0:
    nota5 = valor // 5
    valor = valor % 5

if (valor // 1) >= 0:
    nota1 = valor // 1
    valor = valor % 1


print(f'notas de 100 = {nota100:.0f}')
print(f'notas de 50 = {nota50:.0f}')
print(f'notas de 10 = {nota10:.0f}')
print(f'notas de 5 = {nota5:.0f}')
print(f'notas de 1 = {nota1:.0f}')
