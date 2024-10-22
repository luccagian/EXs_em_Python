"""
Crie um algoritmo que leia o peso e a altura de uma pessoa e calcule o IMC (índice de
massa corpórea) de acordo com a fórmula: IMC = peso / altura^2.
IMC Resultado
0 a 19          Muito Magro
20 a 25         Normal
26 a 30         Sobrepeso
31 a 40         Obeso
Acima de 40     Obesidade Grave
"""

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

IMC = peso/altura**2

if IMC == 0 and IMC <= 19:
    print('Indice muito magro')
if IMC >= 20 and IMC <= 25:
    print('Indice normal')
if IMC >= 26 and IMC <= 30:
    print('Sobrepeso')
if IMC >= 31 and IMC <= 40:
    print('Obeso')
if IMC > 40:
    print('Obesidade grave')
