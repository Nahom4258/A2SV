class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        
        ans.append(celsius + 273.15)
        ans.append((celsius * (9/5)) + 32)
        
        return ans