class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        for i in range(len(queries)):
            queries[i] = self.f(queries[i])
        for i in range(len(words)):
            words[i] = self.f(words[i])

        for query in queries:
            count = 0
            for i in range(len(words)):
                if query < words[i]:
                    count += 1
            ans.append(count)
        print('ans: ', words)

        return ans

    def f(self, word):
        word = list(word)
        word.sort()

        return word.count(word[0])