class RandomizedSet:

    def __init__(self):
        self.found = defaultdict(list)
        self.arr = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val == -3:
            print('ins: ', self.arr, self.found, val)
        if not self.found[val]:
            self.arr.append(val)
            self.found[val].append(self.count)
            self.count += 1
            if val == -3:
                print('insert: ', self.arr, self.found)
            return True

        return False

    def remove(self, val: int) -> bool:
        # if val == -3:
            # print('arr: ', self.arr, val, self.found)
        if self.found[val]:
            rem_val = self.arr[-1]
            # print('arr: ', self.arr, self.found, val, rem_val, self.count)
            val_i = self.found[val].pop()
            if self.count > 1 and rem_val != val:
                self.arr[val_i] = rem_val
                self.found[rem_val][self.found[rem_val].index(self.count-1)] = val_i
            self.arr.pop()
            self.count -= 1
            # print('after: ', self.arr)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()