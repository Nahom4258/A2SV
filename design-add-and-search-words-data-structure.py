class WordDictionary:

    def __init__(self):
        self.children = dict()
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordDictionary()
            
            curr = curr.children[ch]

        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, curr):
            if idx >= len(word):
                return curr.end

            curr_ch = word[idx]

            if curr_ch not in curr.children and curr_ch != '.':
                return False

            ans = False
            if curr_ch == '.':
                for ch in curr.children:
                    ans = ans or dfs(idx+1, curr.children[ch])
            else:
                if curr_ch not in curr.children:
                    return False
                else:
                    ans = ans or dfs(idx+1, curr.children[curr_ch])

            return ans

        return dfs(0, self)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)