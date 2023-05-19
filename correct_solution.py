num = input()
ans = input()
if len(num) == 1 :
    if num == ans:
        print('OK')
    else:
        print('WRONG_ANSWER')
else:
    given = [0 for _ in range(len(num))]
    for i in range(len(num)):
        given[i] = int(num[i])
    given.sort()
    if given[0] == 0:
        i = 0
        while i < len(given) and given[i] == 0:
            i += 1
        given[0], given[i] = given[i],given[0]
    num = 0
    for i in given:
        num *= 10
        num += i
 
    if str(num) == ans:
        print('OK')
    else:
        print('WRONG_ANSWER')