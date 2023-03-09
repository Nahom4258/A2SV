class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(curr, path):
            if curr > n + 1:
                return

            if len(path) == k:
                ans.append(path[::])
                return

            path.append(curr)
            helper(curr+1, path)
            path.pop()
            helper(curr+1, path)

        helper(1, [])

        return ans