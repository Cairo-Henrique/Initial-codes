from time import sleep
ser = 1
result = 0
numerador = 0
denominador = 0
term = 0
cont = 0
n = 2
while True:
    result += 1/ser
    term += 1
    print(f'S{term} = {result}')
    ser *= 2
    if result + 1/ser == result:
        numerador = result
        break
while True:
    numerador *= 10
    cont += 1
    if numerador == int(numerador):
        denominador = 10**(cont)
        print(f'{numerador/denominador} = {numerador}/{denominador}')
        break
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