class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) < 2:
            return int(tokens[0])
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                value2 = stack.pop()
                value1 = stack.pop()
                res = 0
                
                if i == '+': 
                    res = int(value1) + int(value2)
                elif i == '-': 
                    res = int(value1) - int(value2)
                elif i == '*': 
                    res = int(value1) * int(value2)
                elif i == '/': 
                    res = int(int(value1) / int(value2))
                
                stack.append(res)
                
            else:
                stack.append(i)
                
        return stack[0]