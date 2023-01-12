class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        # append variable is added b/c appending inside while loop causes n^2 time complexity
        append = False
        
        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
                if pointer == 0:
                    # append = True replaces digit.insert(0, 1) to insert outside the while loop
                    append = True
                    break
            else:
                digits[pointer] += 1
                break
            
            pointer -= 1
            
        if append:
            digits.insert(0, 1)
            
        return digits