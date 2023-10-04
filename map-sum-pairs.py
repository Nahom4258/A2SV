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

    def find(self, prefix, key_val):
        # check if prefix exists
        curr = self
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]

        # get the additions of the words
        def find_val(curr, arr):
            ans = 0
            curr_key = arr
            if curr.end:
                ans += key_val[''.join(curr_key)]

            for ch in curr.children:
                ans += find_val(curr.children[ch], arr+[ch])

            return ans

        return find_val(curr, list(prefix))

    def __repr__(self):
        return str(self.children) + '\n'

class MapSum:

    def __init__(self):
        self.key_val = defaultdict(int)
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.key_val[key] = val
        self.trie.add(key)

    def sum(self, prefix: str) -> int:
        return self.trie.find(prefix, self.key_val)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)