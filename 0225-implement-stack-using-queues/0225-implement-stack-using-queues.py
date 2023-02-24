class MyStack:

    def __init__(self):
        self.stack = []
        self.q2 = []

    def push(self, x: int) -> None:
        for i in range(len(self.stack)):
            self.q2.append(self.stack[i])
        self.stack = []
            
        self.stack.append(x)
        
        for i in range(len(self.q2)):
            self.stack.append(self.q2[i])
        self.q2 = []

    def pop(self) -> int:
        for i in range(len(self.stack)):
            self.q2.append(self.stack[i])
        self.stack = []
            
        popped = self.q2[0]
        del self.q2[0]
        
        for i in range(len(self.q2)):
            self.stack.append(self.q2[i])
        self.q2 = []
            
        return popped

    def top(self) -> int:
        for i in range(len(self.stack)):
            self.q2.append(self.stack[i])
        self.stack = []
            
        top = self.q2[0]
        
        for i in range(len(self.q2)):
            self.stack.append(self.q2[i])
        self.q2 = []
            
        return top

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()