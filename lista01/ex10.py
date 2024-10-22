"""
Escreva um programa para ler as seguintes informações de um funcionário: Nome,
idade, cargo e o seu salário bruto.
Considere:
a) O salário bruto teve um reajuste de 38%.
b) O funcionário receberá uma gratificação de 20% do salário bruto.
c) O salário total é descontado em 15%.
Faça um algoritmo para:
- Imprimir Nome, idade e cargo.
- Imprimir o salário bruto.
- Imprimir o salário líquido.

"""

nome = input("Seu nome: ")
idade = int(input('Sua idade: '))
cargo = input('Seu Cargo: ')

sal_brut = int(input(' Digite seu salário: '))

reaj = sal_brut*1.38
grat = sal_brut*0.20

sal_liq = (reaj + grat)

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Cargo: {cargo}')
print(f'Salário liquido: {sal_liq}')
