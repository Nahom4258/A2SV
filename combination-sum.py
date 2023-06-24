class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(index, curr, sum, ans):
            if sum == target:
                ans.append(curr[::])
            if sum > target:
                return

            for i in range(index, len(candidates)):
                backtrack(i, curr+[candidates[i]], sum+candidates[i], ans)

            return

        ans = []
        backtrack(0, [], 0, ans)

        return ans