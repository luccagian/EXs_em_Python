"""
 Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura):
- Homens: (72.7 ∗ h) − 58
- Mulheres: (62.1 ∗ h) − 44.7
"""

sexo = input('qual o seu sexo? [M/F]')
altura = float(input('digite sua altura: '))

if sexo.upper() == 'M':
    peso =(72.7*altura) - 58
    print(f'seu peso ideal é: {peso:.2f}')
else:
    peso = (62.1*altura)-44.7
    print(f'seu peso ideal é: {peso:.2f}')

