class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        maxim = max(c.values())
        temp = defaultdict(lambda: [-1, -inf])
        
        max_keys = dict()
        for i in range(n):
            num = nums[i]
            if c[num] == maxim:
                st, end = temp[num]
                if st == -1:
                    st = i
                end = max(end, i)
                temp[num] = [st, end]

        # print('te: ', temp)
        a, b = min(temp.values(), key=lambda x: x[1]-x[0])

        return abs(b-a+1)