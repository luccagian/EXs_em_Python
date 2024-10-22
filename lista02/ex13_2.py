"""
Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa
de 1% para carros fabricados antes de 1990 e uma taxa de 1.5% para os fabricados de
1990 em diante, a taxa está incidindo sobre o valor de tabela do carro. Escreva um
programa que leia o ano e o preço do carro e a seguir calcula e imprime imposto a ser pago
ano = int(input('Digite o ano de seu carro:'))
valorcarro = int(input('Digite o preço do carro:'))
"""

if ano < 1990:
    valorcarro =  1.001*valorcarro
    print(f'imposto a ser pago:{valorcarro:.2f}')
elif ano > 1990:
    valorcarro = 1.0015*valorcarro
    print(f'imposto a ser pago:{valorcarro:.2f}')
