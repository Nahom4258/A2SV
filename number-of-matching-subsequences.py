class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False
        self.count = 0

    def add(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()

            curr = curr.children[ch]

        curr.end = True
        curr.count += 1

    def find(self, word):
        curr = self
        n = len(word)

        def f(idx, curr, parent):
            if idx >= n and not curr.children:
                # print("pa: ", parent)
                return curr.count
            if idx >= n and curr.children:
                return 0

            found = False
            ans = 0
            for i in range(idx, n):
                if parent == word[i] or parent == '*':
                    if curr.end:
                        # print('here', parent, i)
                        ans += curr.count
                    found = True
                    for ch in curr.children:
                        ans += f(i+1, curr.children[ch], ch)
                    break

            if not found:
                return 0

            return ans

        return f(-1, curr, '*')

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)

        return trie.find(s)