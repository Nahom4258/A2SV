class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            st, end = edges[i]
            graph[st].append((end, succProb[i]))
            graph[end].append((st, succProb[i]))

        prob = [-inf] * n
        prob[start_node] = 0
        visited = set()

        max_heap = [(-1, start_node)]

        while max_heap:
            curr_prob, curr_node = heapq.heappop(max_heap)
            curr_prob = -curr_prob

            if curr_node == end_node:
                return curr_prob

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for neigh, w in graph[curr_node]:
                d = curr_prob * w
                if neigh not in visited and d > prob[neigh]:
                    prob[neigh] = d
                    heapq.heappush(max_heap, (-d, neigh))

        return 0