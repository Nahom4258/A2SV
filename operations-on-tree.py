class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        self.parent = parent
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)

        # (locked, user who locked)
        self.state = [(False, -1) for i in range(len(parent))]

        # print('par: ', parent)
        # print('graph: ', self.graph)

    def lock(self, num: int, user: int) -> bool:
        state, locker_user = self.state[num]
        
        # if the node is already locked
        if state:
            return False
        else:
            self.state[num] = (True, user)
            return True

        return True

    def unlock(self, num: int, user: int, upgrade_unlock=False) -> bool:
        state, locker_user = self.state[num]

        # if node is locked
        if state:
            if user == locker_user or upgrade_unlock:
                self.state[num] = (False, -1)
                return True
            else:
                return False
        else:
            return False

        return True

    def upgrade(self, num: int, user: int) -> bool:
        '''
            3 conditions: 
                - node is unlocked
                - node has at least 1 locked descendant(by any user)
                - node doesn't have any locked ancestors
        '''
        state, locker_user = self.state[num]

        # if node is locked, return False
        if state:
            return False

        # check if node has at least 1 locked descendant(locked by any user)
        visited = set()
        locked_descendants = 0

        def dfs(node):
            nonlocal locked_descendants
            state, locker_user = self.state[node]
            if state:
                locked_descendants += 1
            visited.add(node)

            for child in self.graph[node]:
                if child not in visited:
                    dfs(child)

        dfs(num)

        # if there are no locked descendants
        # print('locked_desc: ', locked_descendants)
        if locked_descendants < 1:
            return False

        # check if node has any locked ancestors
        node = num
        found_ancestor = False
        while node != -1: 

            if self.state[node][0]: 
                found_ancestor = True
                break
            node = self.parent[node]

        if found_ancestor:
            return False

        # if it passed all those check, we can execute the upgrade operation
        visited = set()
        def unlock_desc(node):
            self.unlock(node, -1, True)
            visited.add(node)

            for child in self.graph[node]:
                if child not in visited:
                    unlock_desc(child)

        unlock_desc(num)

        self.state[num] = (True, user)

        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)