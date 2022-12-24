class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        left_pointer = 0
        right_pointer = 1
        
        arr.sort()
        
        # iterate through using two pointers
        while right_pointer <= len(arr) - 1 and left_pointer <= len(arr) - 2:
            # if both values are +ve
            if arr[right_pointer] >= 0 and arr[left_pointer] >= 0:
                if arr[right_pointer] == 2 * arr[left_pointer]:
                    return True
                elif arr[right_pointer] < 2 * arr[left_pointer]:
                    right_pointer += 1
                else:
                    left_pointer += 1
                    right_pointer = left_pointer + 1
                
            # if both values are -ve
            elif arr[right_pointer] < 0 and arr[left_pointer] < 0:
                if arr[left_pointer] == 2 * arr[right_pointer]:
                    return True
                elif arr[left_pointer] > 2 * arr[right_pointer]:
                    right_pointer += 1
                else:
                    left_pointer += 1
                    right_pointer = left_pointer + 1
                    
            # double of -ve value can't be +ve and vise versa
            else:
                left_pointer += 1
                right_pointer = left_pointer + 1
                
        return False