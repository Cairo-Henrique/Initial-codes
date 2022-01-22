print('Checar se o número é primo')
m = int(input('Digite o número: '))
print('-'*16)
n = 2
while True:
    if int(m/n) == m/n:
        if n == m:
            print('É primo')
        else:
            print('Não é primo')
            print('O menor divisor é:',n)
            print('O maior divisor é:',int(m/n))
        break
    n += 1