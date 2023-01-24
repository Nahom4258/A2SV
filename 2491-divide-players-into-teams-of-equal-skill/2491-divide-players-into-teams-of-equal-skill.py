class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left_ptr = 0
        right_ptr = len(skill) - 1
        equal_sum = skill[left_ptr] + skill[right_ptr]
        _sum = 0
        
        while left_ptr < right_ptr:
            if skill[left_ptr] + skill[right_ptr] == equal_sum:
                # action
                _sum += (skill[left_ptr] * skill[right_ptr])
                left_ptr += 1
                right_ptr -= 1
            else:
                return -1
            
        return _sum