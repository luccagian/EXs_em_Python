par = 0
lista = []

for i in range(10):
    n = int(input(f'numero {i+1} da lista: '))
    lista.append(n)

maior = max(lista)
menor = min(lista)
soma = sum(lista)
media = soma / 10

for n in lista:
    if n % 2 == 0:
        par += 1

menMed = []

for n in lista:
    if media > n:
        menMed.append(n)       

print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')
print(f'Qtd de  numeros pares: {par}')
print(f'media dos numeros da lista: {media}')
print(f'Numeros menores que a media: {menMed}')