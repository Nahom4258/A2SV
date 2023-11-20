class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if len(s) < 10:
            return []

        ans = []
        c = defaultdict(int)

        c[s[0:10]] += 1
        
        temp = deque(s[0:10])
        for i in range(10, n):
            temp.popleft()
            temp.append(s[i])
            c[''.join(temp)] += 1

        return [key for key, val in c.items() if val > 1]