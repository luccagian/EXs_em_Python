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