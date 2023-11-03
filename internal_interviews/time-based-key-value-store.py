class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.binary_search(key, timestamp)
    
    def binary_search(self, key, timestamp):
        key_val = self.time_map[key]
        left, right = 0, len(key_val)-1
        ans = ''

        while left <= right:
            mid = (left+right) // 2

            if key_val[mid][0] <= timestamp:
                ans = key_val[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)