class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr

            copy = arr[::]
            left_half, right_half, pivot_val = self.pivot((len(copy)-1)//2, copy)
            left = quicksort(left_half)
            right = quicksort(right_half)

            return left + [pivot_val] + right
            
        return quicksort(nums)[len(nums)-k]

    def pivot(self, pivot, arr):
        left_half = []
        right_half = []

        for i in range(len(arr)):
            if arr[i] <= arr[pivot] and i != pivot:
                left_half.append(arr[i])
            elif arr[i] > arr[pivot] and i != pivot:
                right_half.append(arr[i])

        return left_half, right_half, arr[pivot]