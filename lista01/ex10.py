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


