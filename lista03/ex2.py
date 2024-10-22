"""
No correio local há somente selos de 3 e de 5 centavos. A taxa mínima para
correspondência é de 8 centavos. Faça um programa que determina o menor número de
selos de 3 e de 5 centavos que completam o valor de uma taxa dada.
Exemplo:
8 centavos: 1 selo de 3 centavos e 1 selo de 5 centavos.
9 centavos: 3 selos de 3 centavos e 0 selo de 5 centavos.
10 centavos: 0 selos de 3 centavos e 2 selos de 5 centavos.
11 centavos: 2 selos de 3 centavos e 1 selo de 5 centavos.
12 centavos: 4 selos de 3 centavos e 0 selo de 5 centavos.
"""
taxa = int(input('Digite a taxa em centavos:'))

selo3 = 3
selo5 = 5
x = 0
y = 0

if taxa < 8:
    print('Taxa mínima não foi correspondida')

if taxa % selo3 == 0:
    x = taxa // selo3

elif taxa % selo5 == 0:
    y = taxa // selo5

else:
    if (taxa % selo5) == 1:
        y = taxa // selo5 
        x = (1 + selo5) // 3 
        y = y - 1
    if (taxa % selo5) == 2:
        y = taxa // selo5 
        x = (2 + (2*selo5)) // 3 
        y = y - 2
    if (taxa % selo5) == 3:
        y = taxa // selo5 
        x = 3 // 3
    if (taxa % selo5) == 4:
        y = taxa // selo5 
        x = (4 + selo5) // 3
        y = y - 1 

print(f'{taxa} centavos: {x} selos de 3 centavos e {y} selos de 5 centavos')
