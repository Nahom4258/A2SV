class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque(rooms[0])

        while queue:
            node = queue.popleft()

            visited.add(node)
            for val in rooms[node]:
                if val not in queue and val not in visited:
                    queue.append(val)

        # print('ans: ', len(visited), 'room:', len(rooms))
        return len(visited) == len(rooms)