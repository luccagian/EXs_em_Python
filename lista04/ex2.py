pe = 1
altm = 0

while pe <= 10:
    pe = pe + 1
    alt = float(input('escreva a altura das pessoas:'))
    if alt > altm:
        altm = alt
print(f'A altura maior é:{altm}')
