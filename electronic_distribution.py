e = int(input('Quantos elétrons? '))
k = e
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
val = 0
if k > 1:
    k = 2
    e = e - k
    l = e
    if l > 7:
        l = 8
        e = e - l
        m = e
        if m > 17:
            m = 18
            e = e - m
            n = e
            if n > 31:
                n = 32
                e = e - n
                o = e
                if o > 31:
                    o = 32
                    e = e - o
                    p = e
                    if p > 17:
                        p = 18
                        e = e - p
                        q = e
                        if q > 7:
                            q = 8
if n == 0:
    val = m
elif o == 0:
    val = n
elif p == 0:
    val = o
elif q == 0:
    val = p
else:
    val = q
if (val == m) and (val > 18):
    n += m - 18
    m = 18
    val = n
if (val == m) and (val > 8) and (val < 19):
    n += m - 8
    m = 8
    val = n
if (val == n) and (m > 18):
    m += n - 18
    n = 18
    val = n
print(f'K = {k} \nL = {l} \nM = {m} \nN = {n} \nO = {o} \nP = {p} \nQ = {q}\n')
if (val == n) and (val > 18):
    o += n - 18
    n = 18
    val = o
if (val == n) and (val > 8) and (val < 19):
    o += n - 8
    n = 8
    val = o
if (val == o) and (n > 18):
    n += o - 18
    o = 18
    val = o
print(f'K = {k} \nL = {l} \nM = {m} \nN = {n} \nO = {o} \nP = {p} \nQ = {q}\n')

if (val == o) and (val > 18):
    p += o - 18
    o = 18
    val = p
if (val == o) and (val > 8) and (val < 19):
    p += o - 8
    o = 8
    val = p
if (val == p) and (o > 18):
    o += p - 18
    p = 18
    val = p
print(f'K = {k} \nL = {l} \nM = {m} \nN = {n} \nO = {o} \nP = {p} \nQ = {q}\n')
if (val == p) and (val > 18):
    q += p - 18
    p = 18
    val = q
if (val == p) and (val > 8) and (val < 19):
    q += p - 8
    p = 8
    val = q
if (val == q) and (p > 18):
    p += q - 18
    q = 18
    val = q
print(f'K = {k} \nL = {l} \nM = {m} \nN = {n} \nO = {o} \nP = {p} \nQ = {q}')
#Devo excluir o 3° if da série de ifs?
