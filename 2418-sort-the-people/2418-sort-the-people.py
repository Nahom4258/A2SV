# using selection sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            minim = i
            for j in range(i, len(heights)):
                if heights[minim] < heights[j]:
                    minim = j
            heights[i], heights[minim] = heights[minim], heights[i]
            names[i], names[minim] = names[minim], names[i]
            
        return names