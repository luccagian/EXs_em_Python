"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera. O
raio é passado por parâmetro.
V = 4/3 ∗ π ∗ R^3
"""
def vol(r):
    v = 4/3 * (3.14 * r**3)
    return v

r = int(input())

volu = vol(r)

print(volu)
