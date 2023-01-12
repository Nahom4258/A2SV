class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        
        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
                if pointer == 0:
                    digits.insert(0, 1)
                    break
            else:
                digits[pointer] += 1
                break
            
            pointer -= 1
            
        return digits