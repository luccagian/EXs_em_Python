"""
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de
idade, sexo (M/F) e salário. Faça um algoritmo que informe:
a) a média de salário do grupo;
b) maior e menor idade do grupo;
c) quantidade de mulheres com salário até R$3000,00.
Encerre a entrada de dados quando for digitada uma idade negativa
"""

ag = int(input('Digite a idade:'))
sal = 0
sex = 0
agma = ag
agme = ag
sal0 = 0
n = 0
medsal = 0
fsal = 0

while ag > 0:
    
    sal = float(input('Digite o salário:'))
    sal0 += sal
    n += 1
    medsal = sal0/n
    
    sex = input('Sexo M/F:')
    
    if ag > agma:
        agma = ag
    if ag < agme:
        agme = ag
    if sex == 'F' and sal < 3000:
        fsal += 1

    ag = int(input('Digite a idade:'))
    
print('média de salário:',medsal)
print('Maior e menor idade:',agma, ':', agme)
print('Quantidades de mulheres com salários até 3 mil:',fsal)
