"""
Um fabricante vendeu 120 unidades de um produto que custa R$40,00 cada. Sobre o
valor vendido, o fabricante paga 40% de imposto. Escreva um programa que calcule o valor
de imposto a ser pago.
"""

uni = 120
preço = 40

imposto = 40/100

arrecadado = (uni * preço) * 40/100

print(f'O valor do imposto a ser pago é de {arrecadado}')
