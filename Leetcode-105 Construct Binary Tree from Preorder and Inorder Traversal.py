# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        di={inorder[i]:i for i in range(len(inorder))}
        self.j=0
        def go(node,l,r,side):
            if l<=r:
                nn=TreeNode(preorder[self.j])
                self.j+=1
                if side=="l":
                    node.left=nn
                    go(nn,l,di[nn.val]-1,"l")
                    go(nn,di[nn.val]+1,r,"r")
                else:
                    node.right=nn
                    go(nn,l,di[nn.val]-1,"l")
                    go(nn,di[nn.val]+1,r,"r")
        head=TreeNode(-1)
        go(head,0,len(inorder)-1,"l")
        return head.left
