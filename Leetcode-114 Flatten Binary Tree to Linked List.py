# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def go(node):
            if node:
                go(node.left)
                if node.left:
                    right=node.right
                    node.right=node.left
                    node.left=None
                    while node.right:
                        node=node.right
                    node.right=right
                    
                go(node.right)
        go(root)
                    
