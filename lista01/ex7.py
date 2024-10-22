"""
 Escreva um programa que leia a quantidade de litros de combustível gasto por um
automóvel, e a distância percorrida. Após isso calcule o valor do rendimento do automóvel
dados em km/l. Exemplo: A distância percorrida de 472 km utilizando 43 litros de
combustível tem um rendimento de aproximadamente 10,97 km/l.
"""

combustivel = float(input("Litros gastos "))
distancia = float(input("KM rodados "))

rendimento = distancia / combustivel

print(f"O rendimento é {rendimento:.2f} Km/L")

# print(" o rendimento é %.2f km/l", %rendimento
# %.0f vai arredondar o valor 
