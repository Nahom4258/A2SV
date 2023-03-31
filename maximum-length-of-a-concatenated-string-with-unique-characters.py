class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxim = 0
        
        def helper(string, i):
            nonlocal maxim
            
            temp_str = ''.join(string)
            if len(temp_str) == len(set(temp_str)):
                maxim = max(maxim, len(temp_str))
            
            for i in range(i, len(arr)):
                if len(arr[i]) == len(set(arr[i])):
                    helper(string+[arr[i]], i+1)
        
        helper([], 0)

        return maxim