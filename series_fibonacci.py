from time import sleep
ser = 1
result = 0
while True:
    result += ser
    print(result)
    ser = result - ser
    sleep(0.8)