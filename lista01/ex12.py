"""
Uma empresa tem para um determinado funcionário uma ficha contendo o nome,
número de horas trabalhadas e o número de dependentes de um funcionário.
Considerando que:
a) A empresa paga 12 reais por hora e 40 reais por dependente.
b) Sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Faça um algoritmo para ler o nome, número de horas trabalhadas e número de
dependentes de um funcionário. Após a leitura, escreva qual o nome, salário bruto, os
valores descontados para cada tipo de imposto e finalmente qual o salário líquido do
funcionário.
"""
nome=input('Digite seu nome:')
num_hora=int(input('Horas trabalhadas:'))
num_dp=int(input('Numero de depedentes:'))

sal_bruto=(12*num_hora)+40*num_dp

imp=(sal_bruto*8.5/100)
imp2=(sal_bruto*0.05)

sal_liq=(sal_bruto-imp)-imp2

print(f'Nome:{nome}')
print(f'Salario bruto:{sal_bruto}')
print(f'Salario menos INSS:{imp}')
print(f'Salario menos IR:{imp2}')
print(f'Salario liquido:{sal_liq}')
