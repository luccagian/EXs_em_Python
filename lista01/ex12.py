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