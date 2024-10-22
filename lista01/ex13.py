"""
Faça um algoritmo que, tendo como dados de entrada a distância total (em Km)
percorrida por um automóvel e a quantidade de combustível em litros consumida para
percorrê-la, calcule o consumo médio de combustível (km / litro).
"""

km = float(input('Km rodados:'))
L = float(input('Litros abastecidos:'))

consumo = km/L

print(f'Consumo médio:{consumo:.2f}')
