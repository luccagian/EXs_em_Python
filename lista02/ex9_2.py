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
