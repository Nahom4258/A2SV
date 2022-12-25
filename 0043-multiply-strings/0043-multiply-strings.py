class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # define necessary variables
        carry = '0'
        temp = ''
        answer = 0
        num1_pointer = max(len(num1), len(num2)) - 1
        num2_pointer = max(len(num1), len(num2)) - 1
        # check which number is bigger & append '0's to the smaller one to make equal to bigger
        new_zeroes = '0' * abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            num2 = new_zeroes + num2
        elif len(num1) < len(num2):
            num1 = new_zeroes + num1
                    
        # iterate through the numbers using a pointer from the end
        while num1_pointer >= 0 or num2_pointer >= 0:
            if num1_pointer < 0:
                answer += int(temp + ('0' * (len(num2) - 1 - num2_pointer)))
                temp = ''
                carry = '0'
                num1_pointer = len(num1) - 1
                num2_pointer -= 1
                continue
            
            calculate = str((int(num1[num1_pointer]) * int(num2[num2_pointer])) + int(carry))
            if len(calculate) == 2 and num1_pointer != 0:
                temp = calculate[1] + temp
                carry = calculate[0]
            else:
                temp = calculate + temp
                carry = '0'
                
            num1_pointer -= 1
                    
        return str(answer)