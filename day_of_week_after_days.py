dia = int(input('Qual dia da semana? (1 a 7) '))
t = int(input('Quantos dias depois? '))
result = (t/7 - int(t/7))*7+dia
if result > 7:
    result -= 7
print(f'{t} dias depois é {round(result)}')
