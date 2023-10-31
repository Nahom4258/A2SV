# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_min(node):
            if not node.left:
                return node

            return find_min(node.left)
        
        def delete(node, key):
            if not node:
                return node
            
            if key < node.val:
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                # case 1: no child
                if not node.left and not node.right:
                    node = None
                # case 2: one child
                elif node.left and not node.right:
                    node = node.left
                elif node.right and not node.left:
                    node = node.right
                # case 3: two children
                else:
                    minim = find_min(node.right)
                    node.val = minim.val
                    node.right = delete(node.right, minim.val)

            return node

        return delete(root, key)