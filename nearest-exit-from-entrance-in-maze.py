class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set([(entrance[0], entrance[1])])
        queue = deque([(entrance[0], entrance[1])])
        counter = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_row = len(maze)
        max_col = len(maze[0])

        found = False

        while queue:
            length = len(queue)

            for _ in range(length):
                row, col = queue.popleft()

                for dirn in directions:
                    new_row, new_col = row+dirn[0], col+dirn[1]
                    if 0<=new_row<max_row and 0<=new_col<max_col and (new_row, new_col) not in visited and maze[new_row][new_col] == '.':
                        # print('checked: ', new_row, ':', new_col, entrance)
                        # check if new coordinate is on border
                        if (new_row in (max_row-1, 0) or new_col in (max_col-1, 0)) and [new_row, new_col] != entrance:
                            # print('founddd!!!')
                            found = True
                            break
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                if found:
                    break

            counter += 1

            if found:
                break

        return counter if found else -1