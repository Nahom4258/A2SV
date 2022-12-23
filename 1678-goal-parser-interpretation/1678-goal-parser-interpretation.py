class Solution:
    def interpret(self, command: str) -> str:
        lp = 0
        ans = ''
        
        while lp <= len(command) - 1:
            if command[lp] == 'G':
                ans += 'G'
                lp += 1
                
            elif command[lp] == '(' and (lp + 1) <= len(command) and command[lp + 1] == ')':
                ans += 'o'
                lp += 2
                
            elif command[lp] == '(' and (lp + 3) <= len(command) and command[lp + 3]:
                ans += 'al'
                lp += 4
                
        return ans