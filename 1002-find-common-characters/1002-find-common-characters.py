class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        compute = []
        ans = []
        
        for index, word in enumerate(words):
            offset = ord('a')
            counter = [0] * 26
            
            for char in word:
                _ascii = ord(char)
                counter[_ascii - offset] += 1
                
            compute.append(counter)
            
        print('ans: ', compute)
        
        for i in range(26):
            minim = 101
            for j in range(len(compute)):
                if compute[j][i] == 0:
                    minim = 0
                    break
                minim = min(minim, compute[j][i])
                
            ans += [chr(i + 97)] * minim
            

        print(ans)
        
        return ans
        