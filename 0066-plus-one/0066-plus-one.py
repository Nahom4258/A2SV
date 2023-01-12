class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        append = False
        
        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
                if pointer == 0:
                    append = True
                    break
            else:
                digits[pointer] += 1
                break
            
            pointer -= 1
            
        if append:
            digits.insert(0, 1)
            
        return digits