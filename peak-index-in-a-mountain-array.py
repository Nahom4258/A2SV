class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 1
        end = len(arr) - 2
        ans = 0

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                start = mid + 1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                end = mid - 1
            else:
                return mid

        return ans