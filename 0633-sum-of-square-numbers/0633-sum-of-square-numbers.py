class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqs = [0]
        for i in range(1, math.ceil(sqrt(c)) + 1):
            sqs.append(i * i)
            
        left_ptr = 0
        right_ptr = len(sqs) - 1
        
        while left_ptr <= right_ptr:
            if sqs[left_ptr] + sqs[right_ptr] == c:
                return True
            elif sqs[left_ptr] + sqs[right_ptr] > c:
                right_ptr -= 1
            else:
                left_ptr += 1
                
        return False
            