"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        total_importance = 0
        
        for employee in employees:
            # graph[id] = [importance, subordinates]
            graph[employee.id].append(employee.importance)
            graph[employee.id].append(employee.subordinates)

        def helper(curr_id, counting):
            if counting:
                nonlocal total_importance
                total_importance += graph[curr_id][0]

            # if there are no subordinates
            if not graph[curr_id][1]:
                return

            for subordinate in graph[curr_id][1]:
                helper(subordinate, (counting or subordinate == id))

            return

        helper(id, True)
                
        return total_importance