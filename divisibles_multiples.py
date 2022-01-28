while True:
    choice = input('Multíplos (m) ou Divisores (d)? ')
    cont = m = d = 0
    if choice == 'm':
        n = int(input('Quer os múltiplos de qual número? '))
        cont = int(input('Até qual número? '))
        m = list(range(n,cont,n))
        print(f'{m} \n{int(cont/n)} múltiplo(s)\n')
    elif choice == 'd':
        n = int(input('Quer os divisores de qual número? '))
        while d <= n/2:
            d += 1
            if n/d == int(n/d):
                print(d)
                cont += 1
        
        print(f'{n}\n\n{n} tem {cont+1} divisores\n')