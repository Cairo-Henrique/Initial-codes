xi = int(input('x! = '))
n = m = 1
while n < xi:
    m += 1
    n *= m
if n == xi:
    print(f'x = {m}')
else:
    print('Ø')