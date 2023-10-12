class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for st, end, w in flights:
            graph[st].append((end, w))

        dist = [inf] * n
        dist[src] = 0
        visited = dict()

        min_heap = [(0, 0, src)]

        while min_heap:
            # print('cur: ', min_heap)
            curr_dist, curr_k, curr_node = heapq.heappop(min_heap)

            if curr_node in visited and visited[curr_node] <= curr_k:
                continue

            visited[curr_node] = curr_k

            if curr_node == dst and curr_k-1 <= k:
                return curr_dist

            for neigh, w in graph[curr_node]:
                d = curr_dist + w
                heapq.heappush(min_heap, (d, curr_k+1, neigh))
                # print('hea: ', min_heap)

        # print('ans: ', dist)

        return -1