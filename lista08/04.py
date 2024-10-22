"""
Preencha um dicionário com as informações de 5 produtos
- Utilize o nome do produto como chave e o preço como valor.
- Solicite os dados ao usuário
- Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50,00.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5}
"""
produtos = {}

for i in range(5):
    prod = input('nome do produto: ')
    preco = float(input('preço do produto: '))
    produtos[prod] = preco

for chv in produtos:
    if produtos[chv] > 50.0:
        print(f'{chv}: {produtos[chv]}')
