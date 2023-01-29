class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        return_val = -1
        if index < self.length:
            current_index = 0
            current_node = self.head
            while current_index < index:
                current_node = current_node.next
                current_index += 1
            return_val = current_node.val
            
        self.printLink()
            
        return return_val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current_index = 0
            prev = None
            current_node = self.head
            while current_index < index:
                prev = current_node
                current_node = current_node.next
                current_index += 1
            new_node.next = prev.next
            prev.next = new_node
            self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        if index == 0 and self.length == 1:
            self.head = None
        elif index == 0 and self.length > 1:
            self.head = self.head.next
        else:
            current_index = 0
            current_node = self.head
            prev = None
            while current_index < index:
                prev = current_node
                current_node = current_node.next
                current_index += 1
            if index == self.length - 1:
                prev.next = None
            else:
                prev.next = prev.next.next
        
        self.length -= 1
    
    def printLink(self):
        print('length: ', self.length)
        disp = self.head
        while disp:
            print(disp.val, end=' ')
            disp = disp.next
        print()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)