# https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    n = input()
    nums = list(map(int, input().split()))

    flag = True if nums[0] > 0 else False
    max_sum = 0

    maxim = nums[0]
    for i in range(len(nums)):
        if flag:
            if nums[i] > 0:
                maxim = max(maxim, nums[i])
            else:
                max_sum += maxim
                maxim = nums[i]
                flag = False
        else:
            if nums[i] < 0:
                maxim = max(maxim, nums[i])
            else:
                max_sum += maxim
                maxim = nums[i]
                flag = True

    max_sum += maxim
    print(max_sum)
