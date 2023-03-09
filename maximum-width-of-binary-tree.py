# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _dict = defaultdict(list)
        ans = []

        def breadth_first(root, idx, level):
            if not root:
                return

            _dict[level].append(idx)
            breadth_first(root.left, 2 * idx, level + 1)
            breadth_first(root.right, (2 * idx) + 1, level + 1)

        breadth_first(root, 1, 0)

        # print(_dict)
        for key in _dict:
            ans.append(max(_dict[key]) - min(_dict[key]) + 1)

        return max(ans)