sexo = input('qual o seu sexo? [M/F]')
altura = float(input('digite sua altura: '))

if sexo.upper() == 'M':
    peso =(72.7*altura) - 58
    print(f'seu peso ideal é: {peso:.2f}')
else:
    peso = (62.1*altura)-44.7
    print(f'seu peso ideal é: {peso:.2f}')

