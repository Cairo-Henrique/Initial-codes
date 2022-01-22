print('Calculadora relativística')
grandeza = str(input('Quer calcular o espaço ou tempo? (s/t) '))
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
    elif escolha == 'v':
        print("em desenvolvimento")
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
    elif escolha == 'v':
        print("Em desenvolvimento")