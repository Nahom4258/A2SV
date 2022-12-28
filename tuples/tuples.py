if __name__ == '__main__':
    n = int(input())
    elems = tuple(map(int, input().split()))
    print(str(hash(elems)))
