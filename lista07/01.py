def quad(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

n = int(input())

if quad(n):
    print('é um quadrado perfeito')
else:
    print('não é um quadrado perfeito')