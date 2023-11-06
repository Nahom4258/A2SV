class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_d = defaultdict(list)
        t_d = defaultdict(list)

        for i in range(len(s)):
            s_d[s[i]].append(i)
            t_d[t[i]].append(i)
            
        return list(s_d.values()) == list(t_d.values())