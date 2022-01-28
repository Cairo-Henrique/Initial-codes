n200 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = n05 = n025 = 0
choice = str(input('Informar disponibilidade das notas (s/n)? '))
while choice == 's':
    try:
        n200 = int(input('De R$200? '))
        n100 = int(input('De R$100? '))
        n50 = int(input('De R$50? '))
        n20 = int(input('De R$20? '))
        n10 = int(input('De R$10? '))
        n5 = int(input('De R$5? '))
        n2 = int(input('De R$2? '))
        n1 = int(input('De R$1? '))
        n05 = int(input('De R$0.50? '))
        n025 = int(input('De R$0.25? '))
        break
    except:
        print('Ocorreu um erro. Tente novamente.')
val = float(input('Quanto quer sacar? '))
if val/200 >= 1:
    if (choice != 's') or (n200 >= int(val/200)):
        print(f'{int(val/200)} cédula(s) de 200 reais')
        val = val - int(val/200)*200
    elif n200 >= 1:
        print(f'{n200} cédula(s) de 200 reais')
        val = val - 200*n200
if val/100 >= 1:
    if (choice != 's') or (n100 >= int(val/100)):
        print(f'{int(val/100)} cédula(s) de 100 reais')
        val = val - int(val/100)*100
    elif n100 >= 1:
        print(f'{n100} cédula(s) de 100 reais')
        val = val - 100*n100
if val/50 >= 1:
    if (choice != 's') or (n50 >= int(val/50)):
        print(f'{int(val/50)} cédula(s) de 50 reais')
        val = val - int(val/50)*50
    elif n50 >= 1:
        print(f'{n50} cédula(s) de 50 reais')
        val = val - 50*n50
if val/20 >= 1:
    if (choice != 's') or (n20 >= int(val/20)):
        print(f'{int(val/20)} cédula(s) de 20 reais')
        val = val - int(val/20)*20
    elif n20 >= 1:
        print(f'{n20} cédula(s) de 20 reais')
        val = val - 20*n20
if val/10 >= 1:
    if (choice != 's') or (n10 >= int(val/10)):
        print(f'{int(val/10)} cédula(s) de 10 reais')
        val = val - int(val/10)*10
    elif n10 >= 1:
        print(f'{n10} cédula(s) de 10 reais')
        val = val - 10*n10
if val/5 >= 1:
    if (choice != 's') or (n5 >= int(val/5)):
        print(f'{int(val/5)} cédula(s) de 5 reais')
        val = val - int(val/5)*5
    elif n5 >= 1:
        print(f'{n5} cédula(s) de 5 reais')
        val = val - 5*n5
if val/2 >= 1:
    if (choice != 's') or (n2 >= int(val/2)):
        print(f'{int(val/2)} cédula(s) de 2 reais')
        val = val - int(val/2)*2
    elif n2 >= 1:
        print(f'{n2} cédula(s) de 2 reais')
        val = val - 2*n2
if (val >= 1):
    if (choice != 's') or (n1 >= int(val)):
        print(f'{int(val)} moeda(s) de 1 real')
        val = val - int(val)
    elif n1 >= 1:
        print(f'{n1} moeda(s) de 1 real')
        val = val - n1
if val >= 0.5:
    if (choice != 's') or (n05 >= int(val/0.5)):
        print(f'{int(val/0.5)} moeda(s) de 50 centavos')
        val = val - int(val/0.5)*0.5
    elif n05 >= 1:
        print(f'{n05} moeda(s) de 50 centavos')
        val = val - 0.5*n05
if val >= 0.25:
    if (choice != 's') or (n025 >= int(val/0.25)):
        print(f'{int(val/0.25)} moeda(s) de 25 centavos')
        val = val - int(val/0.25)*0.25
    elif n025 >= 1:
        print(f'{n025} moeda(s) de 25 centavos')
        val = val - 0.25*n025
if val != 0:
    print(f'Faltam R${val:.2f}!')
#adicionar opção de calcular troco (hard)
