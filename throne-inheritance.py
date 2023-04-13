class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family_tree = defaultdict(list)
        self.family_tree[kingName].append(1)
        

    def birth(self, parentName: str, childName: str) -> None:
        self.family_tree[parentName].append(childName)
        self.family_tree[childName].append(1)

    def death(self, name: str) -> None:
        self.family_tree[name][0] = 0

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        if self.family_tree[self.kingName][0] == 1:
            ans.append(self.kingName)
        visited = set()

        def helper(parent):

            visited.add(parent)
            for i in range(1, len(self.family_tree[parent])):
                if self.family_tree[parent][i] not in visited:
                    if self.family_tree[self.family_tree[parent][i]][0] == 1:
                        ans.append(self.family_tree[parent][i])
                    helper(self.family_tree[parent][i])

        helper(self.kingName)

        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()