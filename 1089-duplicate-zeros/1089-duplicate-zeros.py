class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        doubled = False
        
        # iterate through the arr and when zero is found arr.insert(i + 1, 0), then pop
        for index in range(len(arr)):
            # check for value to be zero
            if arr[index] == 0 and not doubled:
                arr.insert(index + 1, 0)
                arr.pop()
                doubled = True
            else:
                doubled = False