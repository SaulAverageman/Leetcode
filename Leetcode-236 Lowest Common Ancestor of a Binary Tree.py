class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.g1=1
        self.arr=[]
        self.se=set()
        self.g2=0
        def go1(node,t1,t2):
            if node:
                if self.g1:
                    self.se.add(node.val)
                if node.val==t1 or node.val==t2:
                    self.g1=0
                    self.g2+=1
                go1(node.left,t1,t2)
                go1(node.right,t1,t2)
                    
                if self.g2==2:
                    self.arr.append(node)

        go1(root,p.val,q.val)
                
        for e in self.arr:
            if e.val in self.se:
                return e
