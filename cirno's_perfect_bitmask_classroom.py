test = int(input())
for _ in range(test):
    num = int(input())
    if num == 1:
        print(3)
        continue
    if num % 2 != 0:
        print(1)
        continue
    result = ['1']
    num >>= 1
    while True:
        if num & 1:
            result.append('1')
            break
        result.append('0')
        num >>= 1
    num >>= 1
    if num > 0:
        result[0] = '0'
    result.reverse()
    temp = int(''.join(result),2)
    print(temp)