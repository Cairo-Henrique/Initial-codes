xi = int(input('x! = '))
n = 0
while n < xi:
    n += 1
    xi /= n
if xi == 1:
    print(f'x = {n}')
else:
    print('Ø')
