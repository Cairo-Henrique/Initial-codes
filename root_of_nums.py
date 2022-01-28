raiz = float(input('digite o número: '))
ind = int(input('digite o índice: '))
n = 0
cont = 0
while True:
    n += 1/10**cont
    if (n**ind) <= raiz:
        print(n)
    else:
        n = n - (1/10**cont)
        cont += 1
    if n == n + (1/10**cont):
        break