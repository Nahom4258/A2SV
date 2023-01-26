def rev(arr):
    l_p = 0
    r_p = len(arr) - 1
    while l_p < r_p:
        arr[l_p], arr[r_p] = arr[r_p], arr[l_p]
        l_p += 1
        r_p -= 1
        
    return arr
        
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr) - 1
        k = []
        maxim = 0
        
        if sorted(arr) == arr:
            return []
        
        while maxim != end+1:
            maxim = 0
            # find maximum
            for i in range(end+1):
                if arr[maxim] < arr[i]:
                    maxim = i
                    
            # print('max val: ', arr[maxim], 'and i: ', maxim)
                
            if maxim == 0:
                k.append(end+1)
                arr = rev(arr[:end+1]) + arr[end+1:]
                # print(arr)
                end -= 1 
            else:
                k.append(maxim+1)
                arr = rev(arr[:maxim+1]) + arr[maxim+1:]
                # print(arr)
                
        return k
                
                
                