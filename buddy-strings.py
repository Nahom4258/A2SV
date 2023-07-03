class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            # if s equals goal, and if there is duplicate, we can swap the duplicates and it would work
            return len(set(s)) != len(s)
        
        # if s != goal
        # check the number of swappable/not correctly positioned chars in s
        swappable = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                swappable.append(i)
            if len(swappable) > 2:
                return False

        # if swappable is not equal to 2, we cannot ONLY swap 2 chars
        if len(swappable) != 2:
            return False
            
        # if swappable is 2, swap and check if we get the goal
        i, j = swappable
        temp = list(s)
        temp[i], temp[j] = temp[j], temp[i]

        return ''.join(temp) == goal