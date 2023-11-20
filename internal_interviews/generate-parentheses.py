class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def helper(opened, closed, arr):
            if opened == closed == n:
                nonlocal ans
                ans.append(''.join(arr[::]))
                return

            # if open > closed
            if opened > closed:
                # open another
                if opened+1 <= n:
                    helper(opened+1, closed, arr+['('])
                # close an open
                helper(opened, closed+1, arr+[')'])
            # if open == closed
            if opened == closed:
                # open new one
                helper(opened+1, closed, arr+['('])
            
            return

        helper(0, 0, [])

        return ans