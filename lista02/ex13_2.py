ano = int(input('Digite o ano de seu carro:'))
valorcarro = int(input('Digite o preço do carro:'))

if ano < 1990:
    valorcarro =  1.001*valorcarro
    print(f'imposto a ser pago:{valorcarro:.2f}')
elif ano > 1990:
    valorcarro = 1.0015*valorcarro
    print(f'imposto a ser pago:{valorcarro:.2f}')