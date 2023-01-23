class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxim = -1
        temp = arr[len(arr) - 1]
        for i in range(len(arr) - 1, 0, -1):
            maxim = max(maxim, temp)
            temp = arr[i-1]
            arr[i-1] = maxim
            
        arr[len(arr) - 1] = -1
                
                
        return arr