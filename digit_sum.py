num = list(input('Informe os algarismos: '))
num.sort() 
result = 0
for i in range(10):
    while str(i) in num:
        result += i
        #remove first term from num:
        num = num[1:]
print(result)