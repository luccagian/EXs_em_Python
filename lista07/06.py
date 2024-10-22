""""
Utilizando a função do exercício anterior, escreva um programa que mostre todos os
números primos de 1 até 1000.
"""

def prim(n):
    if n <= 1:
        return False 
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primo = prim

print(primo)
 
