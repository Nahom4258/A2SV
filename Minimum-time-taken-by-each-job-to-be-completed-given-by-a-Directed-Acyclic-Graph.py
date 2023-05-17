from collections import defaultdict, deque


from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> List[int]:
        time = [0] * n
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        # construct the graph
        for fr, to in edges:
            graph[fr].append(to)
            indegree[to] += 1
            
        # print('inde: ', indegree)
        visited = set()
        queue = deque()
        
        for i in range(n):
            if not indegree[i+1]:
                visited.add(i+1)
                queue.append(i+1)
         
        time_elapsed = 1    
        while queue:
            length = len(queue)
            
            for _ in range(length):
                curr = queue.popleft()
                time[curr-1] = time_elapsed
                
                for n in graph[curr]:
                    indegree[n] -= 1
                    
                    if indegree[n] < 1:
                        queue.append(n)
                        
            time_elapsed += 1
        
        time = list(map(str, time))
        
        return ' '.join(time)


#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends