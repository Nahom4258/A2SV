class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = defaultdict(int)
        changed.sort()
        
        for i in range(len(changed)):
            counter[changed[i]] += 1

        ans = []

        if len(changed) % 2 != 0:
            return []

        found = True
        for i in range(len(changed)):
            if counter[changed[i]] and not counter[changed[i]*2]:
                found = False
                break
            if counter[changed[i]] and counter[changed[i]*2]:
                counter[changed[i]] -= 1
                ans.append(changed[i])
                counter[changed[i]*2] -= 1

        return ans if found else []