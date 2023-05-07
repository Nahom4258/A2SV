class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        temp = []

        for key in counter:
            temp.append((-counter[key], key))

        heapq.heapify(temp)

        print('ans: ', temp)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(temp)[1])

        return ans