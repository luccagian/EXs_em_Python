"""
Crie uma função que receba três valores (obrigatoriamente maiores que zero),
representando as medidas dos três lados de um triângulo. Elabore funções para:
(a) Determinar se eles lados formam um triângulo, sabendo que:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros
dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo.
Sendo que:
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes
"""

x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite um ultimo valor:'))

def tri (x,y,z):
    if (x+y)>z and (y+z)>x and (z+x)>y:
        print('forma um triagulo')
        if  x == y == z:
            cat  = 'Eqilátero'
        elif x == y or y == z or z == x:
            cat = 'Isósceles'
        elif x != y != z:
            cat = 'Escaleno'
    else:
            print('Não ira formar um triângulo')
    return cat

tran = tri(x,y,z)

print(tran)
