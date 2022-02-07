print('Calculadora relativística')
grandeza = str(input('Quer calcular utilizar a fórmula do espaço ou do tempo? (s/t) '))
if (grandeza == 'tempo') or (grandeza == 't'):
    escolha = str(input('O que quer calcular? (movementtime, resttime ou v) '))
    if escolha == 'movementtime':
        t = float(input('Informe o tempo que passou para o referencial em repouso: '))
        v = float(input('Informe a velocidade do referencial em movimento em m/s: '))
        gama = 1/((1-(v**2/89875517873681764))**0.5)
        print("∆t' =",t*gama)
    elif escolha == 'resttime':
        t = float(input('Informe o tempo que passou para o referencial em movimento: '))
        v = float(input('Informe a velocidade do mesmo referencial em movimento em m/s: '))
        gama = 1/((1-(v**2/89875517873681764))**0.5)
        print("∆t =",t/gama)
    elif escolha == 'velocidade' or escolha == 'v':
        t = float(input('Informe o tempo que passou para o referencial em repouso: '))
        t0 = float(input('Informe o tempo que passou para o referencial em movimento: '))
        print('V =',(-t**2/t0**2+1)**0.5*299792458)
if (grandeza == 'espaco') or (grandeza == 'espaço') or (grandeza == 's'):
    escolha = str(input('O que quer calcular? (movementlength, restlength ou v) '))
    if escolha == 'movementlength':
        L = float(input('Informe o comprimento para o referencial em repouso: '))
        v = float(input('Informe a velocidade do referencial em movimento em m/s: '))
        gama = 1/((1-(v**2/89875517873681764))**0.5)
        print("L' =",L/gama)
    elif escolha == 'restlength':
        L = float(input('Informe o comprimento para o referencial em movimento: '))
        v = float(input('Informe a velocidade do mesmo referencial em movimento em m/s: '))
        gama = 1/((1-(v**2/89875517873681764))**0.5)
        print("L =",L*gama)
    elif escolha == 'velocidade' or escolha == 'v':
        print('Em desenvolvimento.')