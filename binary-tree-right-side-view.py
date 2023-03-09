# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        _dict = defaultdict(list)
        ans = []

        def breadth_first(root, level):
            if not root:
                return

            _dict[level].append(root.val)
            breadth_first(root.left, level + 1)
            breadth_first(root.right, level + 1)

        breadth_first(root, 0)

        for key in _dict:
            ans.append(_dict[key][-1])

        return ans