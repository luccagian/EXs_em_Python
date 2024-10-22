"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: "Empréstimo não concedido", caso
contrário imprima: "Empréstimo concedido".
"""

sal = float(input('seu salario: '))
prest = float(input('valor da prestação: '))


if prest > (sal*20/100):
    print('emprestimo não concedido')
else:
    print('emprestimo concedido')
