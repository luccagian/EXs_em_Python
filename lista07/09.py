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