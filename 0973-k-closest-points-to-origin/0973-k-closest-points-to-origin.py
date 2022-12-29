
# calculate distance
def distance(point: List[int]) -> int:
    return sqrt(point[0] ** 2 + point[1] ** 2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # variables
        distance_dict = dict()
        answer = []
        
        # store distance as value & index as key
        for index, point in enumerate(points):
            distance_dict[index] = distance(point)
            
        # sort the dictionary
        distance_dict = dict(sorted(distance_dict.items(), key=lambda item: item[1]))
        
        # append upto k
        for index, key in enumerate(distance_dict):
            answer.append(points[key])
            if index == k - 1:
                break
                
        return answer