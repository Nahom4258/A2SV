class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.deleteNode(node)
            self.addAfterHead(node)
            return self.dict[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.deleteNode(node)
            self.addAfterHead(node)
            node.value = value
        else:
            if len(self.dict) >= self.capacity:
                node = self.tail.prev
                self.deleteNode(node)
                del self.dict[node.key]
                
            node = Node(key, value)
            self.addAfterHead(node)
            self.dict[key] = node
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def addAfterHead(self, newNode):
        temp = self.head.next
        self.head.next = newNode
        newNode.next = temp
        temp.prev = newNode
        newNode.prev = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)