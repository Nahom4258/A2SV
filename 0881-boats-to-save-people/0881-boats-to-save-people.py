class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left_ptr = 0
        right_ptr = len(people) - 1
        
        boats = 0
        
        people.sort()
        
        while left_ptr < right_ptr:
            if people[right_ptr] >= limit or people[left_ptr] + people[right_ptr] > limit:
                boats += 1
                right_ptr -= 1
            elif people[left_ptr] + people[right_ptr] <= limit:
                boats += 1
                left_ptr += 1
                right_ptr -= 1
            
            if left_ptr == right_ptr:
                boats += 1
                
        return boats