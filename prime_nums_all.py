n = 1
m = 2
cont = 0
while m <= 1000:
    n += 1
    if int(m/n) == m/n:
        if n == m:
            print(m)
            cont += 1
        n = 1
        m += 1
print('Quantidade de números primos:',cont)