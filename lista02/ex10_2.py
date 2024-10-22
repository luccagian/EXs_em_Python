nome = input('Digite se unome completo')

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
n3 = float(input('Digite a terceira nota'))

media = (n1 + n2 + n3)/ 3

if media >= 7:
    print(f'{nome}, Aprovado')
if media >= 5.1 and media <= 6.9:
    print(f'{nome}, Recuperação')
elif media <= 5:
    print(f'{nome}, Reprovado')