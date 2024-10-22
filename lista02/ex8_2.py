"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:
Categoria Idade
Infantil A    5 a 7
Infantil B    8 a 10
Juvenil A     11 a 13
Juvenil B     14 a 17
Sênior maiores de 18 anos
"""

idade = int(input('Digite sua idade: '))

if idade >= 5 and idade <= 7:
    print('classe: Infantil A')
if idade >= 8 and idade <= 10:
    print('classe: Infantil B')
if idade >= 11 and idade <= 13:
    print('classe: Juvenil A')
if idade >= 14 and idade <= 17:
    print('classe: Juvenil B')
if idade >= 18:
    print('Sênior')
