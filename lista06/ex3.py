n = int(input())
b = 1
c = 1

for i in range(n):
    if i <= 1:
        print('1')
    else:
        soma = b + c
        b = c
        c = soma 
        print(soma)
