class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        union_graph = dict()
        top_edge = set()
        bottom_edge = set()
        for i in range(row):
            for j in range(col):
                union_graph[(i, j)] = (i, j)
                if i == 0:
                    top_edge.add((i, j))
                if i == row-1:
                    bottom_edge.add((i, j))
                
        def find(a):
            if union_graph[a] != a:
                union_graph[a] = find(union_graph[a])

            return union_graph[a]

        def union(a, b):
            rep_a, rep_b = find(a), find(b)

            if rep_a != rep_b:
                if (rep_a in top_edge and rep_b in bottom_edge) or (rep_a in bottom_edge and rep_b in top_edge):
                    return True

                # if a is edge
                if rep_a in top_edge or rep_a in bottom_edge:
                    union_graph[rep_b] = rep_a
                elif rep_b in top_edge or rep_b in bottom_edge:
                    union_graph[rep_a] = rep_b
                else:
                    union_graph[rep_a] = rep_b

            return False

        # print('prev: ', union_graph)
        # print('cehc: ', [[x[0]-1, x[1]-1] for x in cells])

        lands = set()
        for i in range(len(cells)-1, -1, -1):
            r, c = cells[i][0]-1, cells[i][1]-1
            # print('------')
            # print([r, c])
            lands.add((r, c))
            
            for d in directions:
                new_r, new_c = r+d[0], c+d[1]
                if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) in lands:
                    if union((r, c), (new_r, new_c)):
                        return i
                    # print('un: ', union_graph)

        return 0