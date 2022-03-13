from datetime import datetime
time = datetime.now()
minu0 = time.minute
seg0 = time.second
micro0 = time.strftime('%f')
input()
time = datetime.now()
minu = time.minute-minu0
seg = time.second-seg0
micro = int(time.strftime('%f')) - int(micro0)
if micro < 0:
    micro += 1000000
    seg -= 1
if seg < 0:
    seg += 60
    minu -= 1
if minu < 0:
    minu += 60
while micro > 999999:
    seg += 1
    micro -= 1000000
while seg > 59:
    minu += 1
    seg -= 60
print(f'{minu}:{seg}.{micro}')