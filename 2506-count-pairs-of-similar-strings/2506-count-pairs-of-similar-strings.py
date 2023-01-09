class Solution:
    def similarPairs(self, words: List[str]) -> int:
        _dict = defaultdict(int)
        counter = 0
        
        # make each string to set, to eliminate repeating letters
        for index in range(len(words)):
            words[index] = ''.join(sorted(''.join(set(words[index]))))
         
        # iterate and count the words
        for word in words:
            _dict[word] += 1
            
        print(_dict)
            
        # count values and add them to counter
        for key in _dict:
            counter += (_dict[key] * (_dict[key] - 1)) // 2
                
        return counter