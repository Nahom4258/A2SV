class Trie():
    def __init__(self):
        self.children = dict()
        self.can_start = False
        self.end = False

    def add(self, word):
        curr = self
        count = 0
        
        can_cont = False
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
                if curr.can_start:
                    can_cont = True
                if can_cont:
                    count += 1

            curr = curr.children[ch]

        if curr.end:
            return True

        curr.end = True

        if count == 1 or len(word) == 1:
            curr.can_start = True
        else:
            curr.can_start = False

        return count == 1 or len(word) == 1

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))

        trie = Trie()
        ans = ''

        for word in words:
            temp = trie.add(word)
            if temp:
                if len(word) == len(ans):
                    ans = min(word, ans)
                else:
                    ans = max(word, ans, key=lambda x: len(x))

        return ans