class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        directions = (1, -1)
        deadends = set(deadends)
        visited = set(['0000'])
        queue = deque(['0000'])

        if '0000' in deadends:
            return -1

        def generate_new_combo(combo, dirn, i):
            combo = list(map(int, combo))

            if combo[i] + dirn == -1:
                combo[i] = 9
            elif combo[i] + dirn == 10:
                combo[i] = 0
            else:
                combo[i] += dirn

            return ''.join(list(map(str, combo)))

        # print('ans; ', generate_new_combo('0900', 1, 1))

        turns = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                combo = queue.popleft()
                if combo == target:
                    return turns

                for dirn in directions:
                    for i in range(4):
                        new_combo = generate_new_combo(combo, dirn, i)

                        if new_combo not in deadends and new_combo not in visited:
                            queue.append(new_combo)
                            visited.add(new_combo)

            turns += 1

        return -1