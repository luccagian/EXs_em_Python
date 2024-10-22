cont = 1
n = int(input('Escreva a quantidades de números:'))
num = 0

while cont <= n:
    if num % 2 == 0:
        num += 2
    cont = cont + 1
    print(num)
    
