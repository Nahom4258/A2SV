class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        postfix_max = [-1] * n
        postfix_max[n-2] = arr[n-1]

        for i in range(n-3, -1, -1):
            postfix_max[i] = max(arr[i+1], postfix_max[i+1])

        postfix_max[-1] = -1
        
        return postfix_max