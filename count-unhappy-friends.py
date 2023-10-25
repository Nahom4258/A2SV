class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        for i in range(n):
            pref = dict()
            for j in range(n-1):
                pref[preferences[i][j]] = j
            preferences[i] = pref

        pair = [0] * n
        for i in range(n//2):
            a, b = pairs[i]
            pair[a] = b
            pair[b] = a

        ans = 0
        for person in range(n):
            x, y = person, pair[person]
            priority_y = preferences[person][y]
            
            if priority_y != 0:
                for key, pri in preferences[person].items():
                    if pri < priority_y:
                        u, v = key, pair[key]
                        priority_v = preferences[key][v]
                        priority_x_in_v = preferences[key][x]
                        if priority_x_in_v < priority_v:
                            ans += 1
                            break

        return ans