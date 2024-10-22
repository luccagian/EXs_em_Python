produtos = {}

for i in range(5):
    prod = input('nome do produto: ')
    preco = float(input('preço do produto: '))
    produtos[prod] = preco

for chv in produtos:
    if produtos[chv] > 50.0:
        print(f'{chv}: {produtos[chv]}')