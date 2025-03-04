class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Only sorting algorithm I can see that has O(nlog(n)) is Merge Sort and Quick Sort.
        # I can implement Merge Sort: uses Divide and Conquer method to sort but uses 
        # more space.

        # Merge Sort steps
        # Divide list into 2 halves
        # Sort each half and merge
        # Repeat step - use recursion

        def merge(left, right):
            sorted_list = []
            l, r = 0, 0

            while l < len(left) or r < len(right):
                if l >= len(left):
                    sorted_list.append(right[r])
                    r += 1
                    continue

                if r >= len(right):
                    sorted_list.append(left[l])
                    l += 1
                    continue

                if left[l] < right[r]:
                    sorted_list.append(left[l])
                    l += 1
                else:
                    sorted_list.append(right[r])
                    r += 1

            return sorted_list

        def divide(l, r):
            if l > r:
                return []
            if l == r:
                return [nums[l]]

            mid = l + ((r-l)//2)

            left = divide(l, mid)
            right = divide(mid+1, r)

            return merge(left, right)

        return divide(0, len(nums)-1)