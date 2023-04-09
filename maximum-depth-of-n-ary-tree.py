"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxim = 0

        if not root:
            return 0
        
        def helper(head, depth):
            if head.children == None:
                return

            nonlocal maxim
            maxim = max(maxim, depth)

            for i in range(len(head.children)):
                helper(head.children[i], depth + 1)

            return
            
        helper(root, 1)

        return maxim