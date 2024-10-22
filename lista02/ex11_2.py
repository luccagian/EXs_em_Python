"""
Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de
um triângulo e, caso positivo, verificar se é um triângulo equilátero, isósceles e escaleno. Se
eles não formarem um triângulo, o programa deve imprimir uma mensagem adequada.
Considere as seguintes propriedades:
- O comprimento de cada lado em um triângulo é menor que a soma dos outros dois
lados;
- Equilátero: tem os comprimentos dos três lados iguais;
- Isósceles: tem os comprimentos de dois lados iguais;
- Escaleno: tem os comprimentos dos três lados diferentes.
"""

print('Verifique se os valores a seguir podem se tornar ou não medidas de um triângulo:')
x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite um ultimo valor:'))

if (x+y)>z and (y+z)>x and (z+x)>y:
    print('É possivel formar um triângulo:')
    if  x == y == z:
        print('Eqilátero')
    elif x == y or y == z or z == x:
        print('Isósceles')
    elif x != y != z:
        print('Escaleno')
else:
    print('Não ira formar um triângulo')
