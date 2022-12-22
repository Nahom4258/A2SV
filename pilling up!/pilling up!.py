T = int(input())

for testcase in range(T):
    n = int(input())
    blocks = [int(x) for x in input().split(' ')]
    # blocks = list(map(int, input().split(' ')))
    
    lp = 0
    rp = len(blocks) - 1
    bigger = max(blocks[0], blocks[len(blocks) - 1])
    ans = "Yes"
    
    while lp < rp:
        if lp == rp:
            if not blocks[lp] <= bigger:
                ans = "No"
                
        if blocks[lp] == blocks[rp] and blocks[lp] <= bigger:
            bigger = blocks[lp]
            lp += 1
            rp -= 1
        elif blocks[lp] > blocks[rp] and blocks[lp] <= bigger:
            bigger = blocks[lp]
            lp += 1
        elif blocks[lp] < blocks[rp] and blocks[rp] <= bigger:
            bigger = blocks[rp]
            rp -= 1
        else:
            ans = "No"
            break
    
    print(ans)
