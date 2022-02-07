from time import sleep
from os import system
print("calculadora de horários")
operacao = input("+ ou -? ")
while operacao == "+":
    while True:
        try:
            dia1 = int(input("informe o primeiro dia: "))
            hora1 = int(input("informe a primeira hora: "))
            minuto1 = int(input("informe o primeiro minuto: "))
            segundo1 = int(input("informe o primeiro segundo: "))
            dia2 = int(input("informe o segundo dia: "))
            hora2 = int(input("informe a segunda hora: "))
            minuto2 = int(input("informe o segundo minuto: "))
            segundo2 = int(input("informe o segundo segundo: "))
            break
        except:
            print('Ocorreu um erro. Tente novamente.')
    somad = dia1 + dia2
    somah = hora1 + hora2
    somamin = minuto1 + minuto2
    somaseg = segundo1 + segundo2
    while somaseg > 59:
        somamin = somamin + 1
        somaseg = somaseg - 60
    while somamin > 59:
        somah = somah + 1
        somamin = somamin - 60
    while somah > 23:
        somad = somad + 1
        somah = somah - 24
    print(somad,'dia(s)',somah,':',somamin,':',somaseg)
    break
while operacao == "-":
    while True:
        try:
            dia1 = int(input("informe o maior dia: "))
            hora1 = int(input("informe a hora do maior dia: "))
            minuto1 = int(input("informe o minuto do maior dia: "))
            segundo1 = int(input("informe o segundo do maior dia: "))
            dia2 = int(input("informe o menor dia: "))
            hora2 = int(input("informe a hora do menor dia: "))
            minuto2 = int(input("informe o minuto do menor dia: "))
            segundo2 = int(input("informe o segundo do menor dia: "))
            break
        except:
            print('Ocorreu um erro. Tente novamente.')
    somad = dia1 - dia2
    somah = hora1 - hora2
    somamin = minuto1 - minuto2
    somaseg = segundo1 - segundo2
    while somaseg < 0:
        somamin = somamin - 1
        somaseg = somaseg + 60
    while somamin < 0:
        somah = somah - 1
        somamin = somamin + 60
    while somah < 0:
        somad = somad - 1
        somah = somah + 24
    print(somad,'dia(s)',somah,':',somamin,':',somaseg)
    break
input('Iniciar timer -> ')
while (somad > 0) or (somah > 0) or (somamin > 0) or (somaseg > 0):
    system("clear")
    print(somad,'dia(s)',somah,':',somamin,':',somaseg)
    somaseg -= 1
    if somaseg < 0:
        somamin = somamin - 1
        somaseg = somaseg + 60
    if somamin < 0:
        somah = somah - 1
        somamin = somamin + 60
    if somah < 0:
        somad = somad - 1
        somah = somah + 24
    sleep(1)
print('Acabou!')