"""
Faça um programa que receba o custo (valor em reais) de um espetáculo teatral e o
preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar,
nesta ordem:
a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do
espetáculo seja alcançado.
b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.
Observe que as quantidades calculadas a serem vendidas devem ser um número inteiro;
portanto, o resultado da quantidade de convites deve ser arredondado para cima, usando a
função matemática apropriada.
"""

from math import ceil

cust = float(input('Custo do show:'))
ingr = float(input('Custo do Ingresso:'))

qnt_pessoas = cust/ingr

lucro = qnt_pessoas * 1.23

print(f'Convites para lucro mínimo:{ceil(qnt_pessoas)}')
print(f'Convites para Lucrar 23%:{ceil(lucro)}')
