class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = {
            (0, 1): {'L': (-1, 0), 'R': (1, 0)},
            (-1, 0): {'L': (0, -1), 'R': (0, 1)},
            (0, -1): {'L': (1, 0), 'R': (-1, 0)},
            (1, 0): {'L': (0, 1), 'R': (0, -1)}
        }

        start = (0, 0, 0, 1)     # (row, col, x_move, y_move)
        for inst in instructions:
            row, col, x_move, y_move = start
            if inst == 'L':
                new_x, new_y = direction[(x_move, y_move)]['L']
                start = (row, col, new_x, new_y)
            elif inst == 'R':
                new_x, new_y = direction[(x_move, y_move)]['R']
                start = (row, col, new_x, new_y)
            else:
                start = (row+x_move, col+y_move, x_move, y_move)

        row, col, x_move, y_move = start

        return (row, col) == (0, 0) or (x_move, y_move) != (0, 1)