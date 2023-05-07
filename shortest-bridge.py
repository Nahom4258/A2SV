class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_row = len(grid)
        max_col = len(grid[0])
        start = None
        found = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row, col)
                    found = True
                    break
            if found:
                break

        # find the first island using dfs
        first_island = set()
        def dfs(row, col):
            first_island.add((row, col))

            for dirn in directions:
                new_row, new_col = row+dirn[0], col+dirn[1]

                if 0 <= new_row < max_row and 0 <= new_col < max_col and (new_row, new_col) not in first_island and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col)

            return

        dfs(start[0], start[1])

        # print('island; ', sorted(first_island))

        # count until we find part of '1' not part of first_island
        count = 0
        queue = deque()
        visited = set()

        for val in list(first_island):
            queue.append(val)
            visited.add(val)

        # print('queu: ', queue)
        # print('visited: ', visited)

        while queue:
            length = len(queue)

            for _ in range(length):
                row, col = queue.popleft()

                for dirn in directions:
                    new_row, new_col = row+dirn[0], col+dirn[1]

                    if 0 <= new_row < max_row and 0 <= new_col < max_col and grid[new_row][new_col] == 1 and (new_row, new_col) not in first_island:
                        return count

                    if 0 <= new_row < max_row and 0 <= new_col < max_col and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            count += 1

        return 0