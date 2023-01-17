# using bubble sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        left_ptr = 0
        right_ptr = 1
        list_size = len(heights)
        
        while left_ptr != right_ptr and list_size > 1:
            if heights[left_ptr] < heights[right_ptr]:
                heights[left_ptr], heights[right_ptr] = heights[right_ptr], heights[left_ptr]
                names[left_ptr], names[right_ptr] = names[right_ptr], names[left_ptr]
            
            left_ptr += 1
            right_ptr += 1
            if right_ptr >= list_size:
                left_ptr = 0
                right_ptr = left_ptr + 1
                list_size -= 1
        
        return names