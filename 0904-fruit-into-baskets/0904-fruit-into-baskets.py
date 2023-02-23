class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        count = 0
        dic = {}
        while r < len(fruits):
            if dic.get(fruits[r]):
                dic[fruits[r]] += 1
            else:
                dic[fruits[r]] = 1
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    dic.pop(fruits[l])
                l += 1
            count = max(count, r - l + 1)
            r += 1

        return count