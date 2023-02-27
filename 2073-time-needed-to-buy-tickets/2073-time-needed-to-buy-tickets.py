class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        count = 0
        
        for i in range(len(tickets)):
            queue.append(i)
            
        while True:
            idx = queue[0]
            tickets[idx] -= 1
            count += 1
            if idx == k and tickets[idx] == 0:
                break
            elif idx != k and tickets[idx] == 0:
                queue.popleft()
                continue
            queue.popleft()
            queue.append(idx)
        
        return count
            