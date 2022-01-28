numerador = float(input('Digite o número decimal: '))
denominador = 0
cont = 0
while True:
    numerador *= 10
    cont += 1
    if numerador == int(numerador):
        denominador = 10**(cont)
        print(f'{numerador/denominador} = {numerador}/{denominador}')
        break
n = 2
while (n <= numerador) or (n <= denominador):
    numerador /= n
    denominador /= n
    if not (numerador == int(numerador)) or not (denominador == int(denominador)):
        numerador *= n
        denominador *= n
        n += 1
    else:
        print('÷',n)
        print(f'{numerador/denominador} = {numerador}/{denominador}')
        n = 2