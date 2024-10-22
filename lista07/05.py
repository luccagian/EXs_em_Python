"""
Faça uma função que receba um número n, como parâmetro, devolve True se ele é
primo, e False, caso contrário. (um número primo tem apenas 2 divisores: 1 e ele mesmo! O
número 1 não é primo!!!)
"""

n = int(input())

def prim(n):
    for i in range(2,n):
        if n % i == 0:
            a = False
        elif n % i != 0:
            a = True
        return a
    
primo = prim(n)

print(primo)
