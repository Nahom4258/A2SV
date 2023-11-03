class SnapshotArray:

    def __init__(self, length: int):
        self.changes = dict()
        self.snap_count = 0
        self.snaps = dict()

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val

    def snap(self) -> int:
        snap_id = self.snap_count
        self.snaps[snap_id] = self.changes.copy()
        self.changes = dict()
        self.snap_count += 1

        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]

        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)