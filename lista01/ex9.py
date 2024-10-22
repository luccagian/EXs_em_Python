"""
Faça um programa que resolva o seguinte problema:
Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três
ganhadores da seguinte forma:
- O primeiro ganhador receberá 46% do prêmio;
- O segundo ganhador receberá 32% do prêmio;
- O terceiro ganhador receberá o restante do prêmio.
Calcule e mostre o valor do prêmio de cada ganhador.
"""

premio = 780000

prim = 46/100 * premio
seg = 32/100 * premio
terc = premio - prim - seg

print(f"Premio do 1 = {prim}")
print(f"Premio do 2 = {seg}")
print(f"Premio do 3 = {terc}")
