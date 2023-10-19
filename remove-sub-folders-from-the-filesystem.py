class Trie:
    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, f):
        curr = self
        f = f.split('/')
        if f[0] == '':
            f = f[1:]

        for i in range(len(f)):
            if f[i] == '':
                f[i] = '/'
            else:
                f[i] = '/'+f[i]

        # print('insert: ', f)

        for name in f:
            if name not in curr.children:
                curr.children[name] = Trie()

            curr = curr.children[name]

        curr.end = True

    def remove(self, f):
        curr = self
        f = f.split('/')
        if f[0] == '':
            f = f[1:]

        for i in range(len(f)):
            if f[i] == '':
                f[i] = '/'
            else:
                f[i] = '/'+f[i]

        for i, name in enumerate(f):
            if name not in curr.children:
                return
            if i == len(f)-1:
                curr.children[name] = Trie()
                break
            curr = curr.children[name]

        # print('remove: ', curr)
    
    def __repr__(self):
        return str(self.children)

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for name in folder:
            trie.insert(name)

        for name in folder:
            trie.remove(name)

        ans = []
        def helper(curr, name):
            nonlocal ans
            if not curr.children:
                ans.append(name)
                return

            # print('curr: ', curr)
            for k, v in curr.children.items():
                helper(curr.children[k], name+[k])

            return

        helper(trie, [])

        for name in ans:
            temp = []

        # print('tt: ', trie, ans)
        return [''.join(name) for name in ans]