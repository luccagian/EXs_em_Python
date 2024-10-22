"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).
Faça um programa em que o usuário entre com o valor e o estado destino do produto e o
programa retorne o preço final do produto acrescido do imposto do estado em que ele será
vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

valor = float(input('digite o valor: '))
estado = input('digite a sigla do estado: ')

if estado.upper() == 'MG':
    imp=valor*1.07
    print(f'o valor real é: {imp}')

elif estado.upper() == 'SP':
    imp=valor*1.12
    print(f'o valor real é: {imp}')

elif estado.upper() == 'RJ':
    imp=valor*1.15
    print(f'o valor real é: {imp}')

elif estado.upper() == 'MS':
    imp=valor*1.08
    print(f'o valor real é: {imp}')

else:
    print('estado inválido')
