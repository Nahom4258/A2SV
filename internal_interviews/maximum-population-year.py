class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        def idx(i):
            return i-1950

        for birth, death in logs:
            years[idx(birth)] += 1
            years[idx(death)] -= 1

        add = 0
        ans = 1950
        maxim = 0
        for i, num in enumerate(years):
            add += num
            if add > maxim:
                ans = i+1950
                maxim = add

        return ans