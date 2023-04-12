class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        visited = set()
        maxim = 0
        counter = 0

        def dfs(curr_bomb):
            nonlocal counter

            visited.add(curr_bomb)
            for i in range(len(bombs)):
                if i != curr_bomb and i not in visited:
                    distance_bn_pts = sqrt((bombs[curr_bomb][0]-bombs[i][0])**2 + (bombs[curr_bomb][1]-bombs[i][1])**2)
                    if bombs[curr_bomb][2] >= distance_bn_pts:
                        counter += 1
                        dfs(i)

        for bomb in range(len(bombs)):
            if bomb not in visited:
                counter = 0
                visited = set()
                dfs(bomb)
                maxim = max(maxim, counter)


        return maxim+1