class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ans = True
        left_pointer = 0
        right_pointer = 0
        
        mydict = dict()
        
        # add the orders into a dictionary, key = letter & value = index
        for i, letter in enumerate(order):
            mydict[letter] = i
            
        for i in range(len(words) - 1):
            left_pointer = 0
            right_pointer = 0
            while left_pointer < len(words[i]) or right_pointer < len(words[i + 1]):
                if not left_pointer < len(words[i]):
                    return True
                if not right_pointer < len(words[i + 1]):
                    return False
                    
                if mydict[words[i][left_pointer]] > mydict[words[i + 1][right_pointer]]:
                    return False
                if mydict[words[i][left_pointer]] < mydict[words[i + 1][right_pointer]]:
                    break
                    
                left_pointer += 1
                right_pointer += 1
            
        return ans