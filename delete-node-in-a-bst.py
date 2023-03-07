# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root, key):
            if not root:
                return None

            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:
                # if node being deleted has 'one' or no children
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                # node contains two children
                inorder_successor = self.inorder_successor(root.right)

                root.val = inorder_successor.val

                root.right = delete(root.right, inorder_successor.val)

                return root

            return root

        return delete(root, key)

    def inorder_successor(self, node):
        res = node
        while res.left:
            res = res.left

        return res