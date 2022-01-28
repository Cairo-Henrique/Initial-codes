i = int(input('Informe o índice: '))
v = int(input('Informe o radicando: '))
n = 2
cont = 0
multiplic = 1
if v**(1/i) == int(v**(1/i)):
    print(v**(1/i))
else:
    while n <= v:
        v = v/n
        cont += 1
        if not (v == int(v)):
            v = v*n**cont
            n += 1
            cont = 0
        elif cont == i:
            multiplic *= n
            print('÷',n)
            print(f'{multiplic}√{int(v)} = {multiplic*v**(1/i)}')
            cont = 0
#Acho que arrumei colocando n**cont
