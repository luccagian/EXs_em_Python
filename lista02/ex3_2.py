sal = float(input('seu salario: '))
prest = float(input('valor da prestação: '))


if prest > (sal*20/100):
    print('emprestimo não concedido')
else:
    print('emprestimo concedido')
