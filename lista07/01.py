"""
Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado
perfeito é um número inteiro não negativo que pode ser expresso como o quadrado de outro
número inteiro. Ex: 1, 4, 9...
"""

def quad(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

n = int(input())

if quad(n):
    print('é um quadrado perfeito')
else:
    print('não é um quadrado perfeito')
