class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()

        counter = 1
        for char in s:
            if char not in visited:
                visited.add(char)
            else:
                counter += 1
                visited = set()
                visited.add(char)

        return counter