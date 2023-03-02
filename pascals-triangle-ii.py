class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def get_row(arr, rowIndex):
            if len(arr) - 1 == rowIndex:
                return arr

            temp = [1]

            for i in range(1, len(arr)):
                temp.append(arr[i-1] + arr[i])

            temp.append(1)
        
            return get_row(temp, rowIndex)
        
        return get_row([1], rowIndex)