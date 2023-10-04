class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
            
        distances = {node: inf for node in range(1, n+1)}
        distances[k] = 0
        visited = set()

        min_heap = [(0, k)]

        while min_heap:
            curr_dist, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for neigh, w in graph[curr_node]:
                distance = curr_dist + w
                if distance < distances[neigh]:
                    distances[neigh] = distance
                    heapq.heappush(min_heap, (distance, neigh))

        if inf in distances.values():
            return -1

        return max(distances.values())