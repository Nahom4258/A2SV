class Trie():
    def __init__(self):
        self.children = dict()
        self.end = False

    def add(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]

        curr.end = True

    def search(self, word: str, arr, pref) -> int:
        # check if prefix exists
        curr = self
        for ch in word:
            if ch not in curr.children:
                return -1
            curr = curr.children[ch]
        
        def dfs(root, running):
            if not root.children:
                key = pref + ''.join(running)
                # print('runnin: ', running, key)
                # print('arr: ', arr)
                return arr[key]

            ret = -1
            if root.end:
                t_key = pref + ''.join(running)
                ret = max(ret, arr[t_key])

            for ch in root.children:
                ret = max(ret, dfs(root.children[ch], running+[ch]))

            return ret

        # print('got: ', dfs(curr, []))
        ans = dfs(curr, [])
        # print('aaa: ', ans)

        return ans

    def __repr__(self):
        return str(self.children) + '\n'

class WordFilter:

    def __init__(self, words: List[str]):
        self.arr = defaultdict(lambda: -1)
        self.trie = Trie()
        
        for i in range(len(words)):
            self.arr[words[i]] = i

        for word in words:
            to_add = word + '|' + word
            while True:
                if to_add[0] == '|':
                    break

                self.trie.add(to_add)
                to_add = to_add[1:]

            self.trie.add(to_add)

    def f(self, pref: str, suff: str) -> int:
        q = suff + '|' + pref
        ans = self.trie.search(q, self.arr, pref)

        if ans != -1:
            return ans
            
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)