# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.out=[]
        
        def go(node,h):
            if node:
                if len(self.out)<h:
                    self.out.append(node.val)
                else:
                    self.out[h-1]=node.val
                go(node.left,h+1)
                go(node.right,h+1)
        
        go(root,1)
        return self.out
