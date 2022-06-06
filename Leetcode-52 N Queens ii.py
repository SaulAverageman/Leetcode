class Solution:
    def totalNQueens(self, n: int) -> int:
        #hard-coded; bad code
        self.out=0
        self.col=["."]*1000
        self.IND=0
        
        def check(i,j):
            for arr in self.col[:self.IND]:
                if arr[1]==j:
                    return 1
                slope=abs(arr[0]-i)/abs(arr[1]-j)
                if slope==1 or slope==-1:
                    return 1
            return 0
        def go(i,n):
            if i==n:
                self.out+=1
                return
            for j in range(n):
                if check(i,j):
                    continue
                self.col[self.IND]=[i,j]
                
                self.IND+=1
                go(i+1,n)
                self.IND-=1
        
        go(0,n)
        return self.out
