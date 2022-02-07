from time import sleep
x = y0 = 0
cont = 1
y = 1
def f(x):
    return x**(1/x)
while x != x+1/10**cont:
    x += 1/10**cont
    y = f(x)
    if y > y0:
        print(f'f({x}) = {y}')
        y0 = y
    else:
        x = x - (1/10**cont)
        cont += 1
        #print(cont)
#Somente dá resultados aproximados
