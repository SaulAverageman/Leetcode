# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.g1=1
        self.arr=[]
        self.se=set()
        def go1(node,t1,t2):
            if self.g1 and node:
                if node.val==t1 or node.val==t2:
                    self.g1=0
                self.se.add(node)
                go1(node.left,p.val,q.val)
                go1(node.right,p.val,q.val)
        
        go1(root,p.val,q.val)
        
        self.g2=0

        def go2(node,t1,t2):
            if node:
                go2(node.left,p.val,q.val)
                go2(node.right,p.val,q.val)
                if node.val==t1 or node.val==t2:
                    self.g2+=1
                if self.g2==2:
                    self.arr.append(node)
        go2(root,p.val,q.val)
            
        
        for e in self.arr:
            if e in self.se:
                return e


        
