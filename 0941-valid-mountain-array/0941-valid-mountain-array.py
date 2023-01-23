class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = True
        count = 0
        
        if len(arr) < 3:
            return False
        
        if arr[0] >= arr[1]:
            return False
        
        for i in range(len(arr) - 1):
            if increasing:
                if arr[i] > arr[i+1]:
                    increasing = False
                    count += 1
                elif arr[i] == arr[i+1]:
                    return False
            else:
                if arr[i] < arr[i+1]:
                    increasing = False
                    count += 1
                elif arr[i] == arr[i+1]:
                    return False
        
        return count == 1