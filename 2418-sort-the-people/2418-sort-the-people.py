# using insertion sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(1, len(heights)):
            j = i - 1
            temp = i
            while j >= 0:
                if heights[temp] > heights[j]:
                    heights[temp], heights[j] = heights[j], heights[temp]
                    names[temp], names[j] = names[j], names[temp]
                    temp -= 1
                    j -= 1
                else:
                    break
            
        return names
            
                