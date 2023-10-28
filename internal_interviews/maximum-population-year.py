class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        for birth, death in logs:
            for i in range(birth, death):
                years[i-1950] += 1

        maxim = max(years)

        for i in range(101):
            if years[i] == maxim:
                return i+1950

        return 0