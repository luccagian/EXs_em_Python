from math import ceil

cust = float(input('Custo do show:'))
ingr = float(input('Custo do Ingresso:'))

qnt_pessoas = cust/ingr

lucro = qnt_pessoas * 1.23

print(f'Convites para lucro mínimo:{ceil(qnt_pessoas)}')
print(f'Convites para Lucrar 23%:{ceil(lucro)}')
