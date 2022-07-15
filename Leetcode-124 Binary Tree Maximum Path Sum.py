# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.out=-10**9
        def go(node):
            if node:
                x=go(node.left)
                y=go(node.right)
                self.out=max(self.out,node.val,node.val+x,node.val+y,node.val+x+y)
                node.val+=max(x,y,0)
                self.out=max(self.out,node.val)
                #print(node.val)
                return node.val
            return 0
        
        go(root)
        
        return self.out
