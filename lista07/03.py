def seg(h,m,s):
    s1 = h * 3600
    s2 = m * 60
    s3 = s * 1
    s = s1+s2+s3
    return s

h = int(input('horas'))
m = int(input('minutos'))
s = int(input('segundos'))

conv = seg(h,m,s)

print(conv)
