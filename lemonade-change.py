class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        def is_change_possible(money):
            target = money - 5
            if money == 5:
                change[5] += 1
                return True
            if target == 5 and change[target] > 0:
                change[5] -= 1
                change[10] += 1
                return True
            if target == 15 and change[5] > 0 and change[10] > 0:
                change[5] -= 1
                change[10] -= 1 
                change[20] += 1
                return True

            if target == 15 and change[5] >= 3:
                change[5] -= 3
                change[20] += 1
                return True

            return False

        for i in range(len(bills)):
            if not is_change_possible(bills[i]):
                return False

        return True