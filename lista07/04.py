"""
) Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida
em graus Fahrenheit. A fórmula de conversão é:
F = C ∗ (9.0/5.0) + 32.0,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius
""" 
def conv(c):
    f = c * (9.0/5.0) * 32.0
    return f 

c = float(input())

temp = conv(c)

print(temp)
