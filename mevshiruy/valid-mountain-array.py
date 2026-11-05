class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) <= 2:
            return False

        '''
        approach: the tip of the mountain is always the maximum number. so we can count the number of the maximum number, and if its more than 1, it means there is another tip, which makes it false
        edit: also, if max number count is 1 and it should also NOT be at start or end, else that would mean its not tip of mountain
        ALSO: make sure that its left and right of max number is decreasing
        '''
        c = Counter(arr)

        if c[max(arr)] != 1:
            return False

        if arr.index(max(arr)) in [0, len(arr)-1]:
            return False

        # left strictly increasing
        for i in range(arr.index(max(arr))-1, -1, -1):
            if arr[i] >= arr[i+1]:
                return False

        # right strictly increasing
        for i in range(arr.index(max(arr)), len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False

        return True