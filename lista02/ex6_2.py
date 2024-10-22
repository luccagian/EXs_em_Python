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
