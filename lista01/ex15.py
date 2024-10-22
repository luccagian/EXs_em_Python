"""
Escreva um programa que leia a largura e altura de uma parede, calcule a área a ser
pintada e a quantidade de tinta necessário para o serviço, sabendo que cada litro de tinta
pinta uma área de 2 metros quadrados
"""

alt=float(input('Altura da parede:'))
larg=float(input('Largura da parede:'))

area=alt*larg
qnt_tinta=area/2 

print(f'Area da parede:{area}')
print(f'Tinta necessaria:{qnt_tinta}')
