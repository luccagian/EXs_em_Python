multas = {
'ABC1234': 150.50,
'DEF5678': 200.75,
'GHI9012': 180.25,
'JKL3456': 100.00,
'MNO7P89': 220.30,
'PQR1S23': 175.60,
'STU5T67': 190.45,
'VWX9U01': 210.20,
'YZA3V45': 160.75,
'BCD789F': 195.80
}

def cad_mult():
    placa = input('digite a placa: ')
    valor = float(input('digite o valor: '))
    multas[placa] = valor

def busq_mult():
    pl = input('digite a placa que deseja buscar: ')
    pl = pl.upper()
    if pl in multas:
        print(f'Placa: {pl}: Multa: {multas[pl]}')
    else:
        print('placa não encontrada')

def list_mult():
    for chv in multas:
        print(f'Placa: {chv}: Multa: {multas[chv]}')

def ord_mult():
    ma = multas[max(multas, key = multas.get)]
    me = multas[min(multas, key = multas.get)]

    for chv in multas:
        if ma == multas[chv]:
            print(f'Maior valor = Placa: {chv}: Multa: {multas[chv]}') 
        if me == multas[chv]:
            print(f'Menor valor = Placa: {chv}: Multa: {multas[chv]}')

def med_mult():
    qt = len(multas)
    soma = 0
    for chv in multas:
        soma = soma + multas[chv]

    med = soma/qt
    print(f'o valor medio das multas é: {med:.2f}')

while True: 
    print("""1 - Cadastrar multa (placa, valor)
2 - Buscar multa pela placa
3 - Listar todas as multas
4 - Exibir placa/multa referente ao valor mais alto e mais baixo
5 - Calcular o valor médio de todas as multas
6 - Sair  \n """)
    opcao = int(input('Digite uma opção do menu:'))

    if opcao == 1:
        cad_mult()
        print('multa cadastrada \n')
         
    if opcao == 2:
        busq_mult()
        print('\n')
    if opcao == 3:
        list_mult()
        print('\n')
    if opcao == 4:
        ord_mult()
        print('\n')
    if opcao == 5:
        med_mult()
        print('\n')
    if opcao == 6:
        print('você saiu')
        break