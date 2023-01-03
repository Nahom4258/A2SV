from collections import defaultdict

t = int(input())

for i in range(t):
    _dict = defaultdict(int)
    _dict['S'] = 0
    _dict['M'] = 1
    _dict['L'] = 2
    size_a = ''
    size_b = ''
    
    shirt_sizes = input().split()
    
    for letter in shirt_sizes[0]:
        if letter not in ['S', 'M', 'L']:
            _dict['0' + letter] += 1
        else:
            size_a = letter
        
    for letter in shirt_sizes[1]:
        if letter not in ['S', 'M', 'L']:
            _dict['1' + letter] += 1
        else:
            size_b = letter
            
    if size_a == size_b:
        if size_b == 'M':
            print('=')
        else:
            if _dict['0X'] > _dict['1X']:
                if size_a == 'S':
                    print('<')
                else:
                    print('>')
            elif _dict['0X'] < _dict['1X']:
                if size_a == 'L':
                    print('<')
                else:
                    print('>')
            else:
                print('=')
    else:
        if _dict[size_a] > _dict[size_b]:
            print('>')
        else:
            print('<')
