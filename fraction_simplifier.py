print('Simplificador de frações')
numerador = int(input('Informe o numerador: '))
denominador = int(input('Informe o denominador: '))
multiplic = 1
n = 2
while (n <= numerador/2) or (n <= denominador/2):
    numerador /= n
    denominador /= n
    if not (numerador == int(numerador)) or not (denominador == int(denominador)):
        numerador *= n
        denominador *= n
        n += 1
    else:
        print('÷',n)
        print(f'{int(numerador)}/{int(denominador)} = {numerador/denominador}')
        multiplic *= n
        n = 2
print(f'Os números foram divididos por {multiplic}')
#mudei a condição do while para /2, talvez isso dê problema pois numerador e denominador ficam mudando
