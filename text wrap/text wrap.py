import textwrap

def wrap(string, max_width):
    s = ''
    pointer = 0
    
    while pointer < len(string):
        if (pointer + max_width) % max_width == 0:
            s = s + '\n' + string[pointer : pointer + max_width]
           
        pointer += 1
    return s[1:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
